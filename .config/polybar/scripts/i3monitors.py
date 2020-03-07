#!/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import subprocess

"""This script is for automatical monitor control. It checks the connected monitors and set them up according to a given command"""

#name of internal monitor
internal_monitor="eDP1"

#See which monitors are connected
xrandr=os.popen("xrandr").readlines()

#Search for connected monitors

best_res={}
current_monitor=""

#Check for conneted monitors and their highest resolution and save it in a dictionary
for line in xrandr:
    pos=line.find("connected")
    if pos != -1:
        if line.find("disconnected") != -1:
            continue
        else:
            current_monitor=line[0:(pos-1)]
            continue
    if current_monitor != "":
        x=int(line[0:line.find("x")])
        y=int(line[line.find("x")+1:line.find("x")+5])
        print(x,y)
        best_res[current_monitor]=[x,y]
        current_monitor=""

#The second monitor is the first connected in the dictonary which isn't the internal Monitor of the Laptop
second=""
for i in best_res:
    if i != internal_monitor:
        second=i
        break

#Check if there is an argument given to the script
if len(sys.argv) > 1:
    order=sys.argv[1]
else:
    order="None"

#Read last configuration
try:
    with open("/home/jroith/.config/polybar/scripts/.screen", "r") as file_in:
        screen_config=file_in.readline()
except:
    with open("/home/jroith/.config/polybar/scripts/.screen", "w") as file_out:
        screen_config=""

screen="DP1"
if screen_config == "":     #no config file found create own by using the internal setting->
    config = "internal"
    num_screens=1
#elif screen_config.find("internal") == -1:
else:
    config, screen, num_screens = screen_config.split(";")
#else:
#    config = "internal"

#If there is a new screen, append it
if int(num_screens) > len(best_res):
    order="internal"
    num_screens="1"

#if there is a new screen, update var num_Screen
if config == "internal" and int(num_screens) < len(best_res):
    order="internal"
    num_screens=str(len(best_res))

#if a monitor is unplugged and the config isn't internal switch back to internal
if config != "internal" and  int(num_screens) > len(best_res):
    order="internal"
    num_screens=str(len(best_res))

#Dictionary with a mapping from the configs to font awesome symbols
icon_set={"internal":"", "external":"", "presentation":""}
skip=False
#Execute command acording to first parameter

#restore last setting
if order == "startup":
    order = config

if order == "internal":
    command="xrandr --output " + internal_monitor + " --auto"
    os.system(command)
    if len(best_res) > 1:
        command="xrandr --output " + second + " --off "  
        os.system(command)
        command="xrandr --output " + second + " --auto " 
        os.system(command)
        command="xrandr --output " + second + " --left-of " + internal_monitor  
        os.system(command)
    else:
        command="xrandr --output " + screen + " --off"
        os.system(command)
elif order == "external" and len(best_res) >1:
    command="xrandr --output " + second + "--auto"
    os.system(command)
    command="xrandr --output "+internal_monitor+" --off"
    os.system(command)
elif order == "presentation" and len(best_res) > 1:
    #Calculate Scaling
    scale_x=1.0 * best_res[internal_monitor][0] / best_res[second][0]
    scale_y=1.0 * best_res[internal_monitor][1] / best_res[second][1]
    command="xrandr --output "  + internal_monitor + " --auto"
    os.system(command)
    command="xrandr --output " + second + " --same-as " + internal_monitor
    os.system(command)
    command="xrandr --output " + second + " --scale " + str(scale_x)+"x"+str(scale_y)
    os.system(command)
elif order == "right" and len(best_res) > 1:
    if config == "internal":
        command = "xrandr --output " + second + " --auto --right-of " + internal_monitor 
        os.system(command)
    elif config == "external":
        command = "xrandr --output "+ internal_monitor +" --auto --right-of " + second
        os.system(command)  
elif order == "left" and len(best_res) > 1:
    if config == "internal":
        command = "xrandr --output "+ second +" --auto --left-of " + internal_monitor 
    elif config == "external":
        command = "xrandr --output "+ internal_monitor +" --auto --left-of " + second
    os.system(command)
else:
    order="None"
    skip=True
    
if not skip:
     os.system("sh /home/jroith/.fehbg")
     #os.system("bash /home/jroith/.start_bar.sh &")

if order == "None" or order == "right" or order == "left":
    print(icon_set[config])
else:
    with open("/home/jroith/.config/polybar/scripts/.screen", "w") as file_out:
#        if order == "internal":
#            file_out.write(order)
#            print icon_set[order]
#        else:
            file_out.write(order+";"+second+";"+str(num_screens))
            print(icon_set[order])
