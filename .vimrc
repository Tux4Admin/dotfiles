""" Grundlegendes Verhalten
set number
set relativenumber
set encoding=utf-8
set spelllang=de_de

""" Keybindings
nmap j gj
nmap k gk

map ,n <ESC>:set nu! relativenumber!<CR>
imap ,n <ESC>:set nu! relativenumber!<CR>
map <F5> <ESC>:set spell! <CR>
imap <F5> <ESC>:set spell! <CR>

""" Syntax
syntax enable
filetype plugin indent on

""" Tab settings
set tabstop=4
set shiftwidth=4
set softtabstop=4

set autoindent
set smartindent

""" remap Capslock to ESC
au VimEnter * silent! !xmodmap -e 'clear Lock' -e 'keycode 0x42 = Escape'
au VimLeave * silent! !xmodmap -e 'clear Lock' -e 'keycode 0x42 = Caps_Lock'


" Navigating with guides
	inoremap ,, <Esc>/<++><Enter>"_c4l
	vnoremap ,, <Esc>/<++><Enter>"_c4l
	map ,, <Esc>/<++><Enter>"_c4l

"""LaTeX
autocmd FileType tex imap ,frame \begin{frame}<Enter><Tab>\frametitle{}<Enter><Enter><++><Enter><Enter><BS>\end{frame}<Enter><Enter><++><Esc>6kf}i
autocmd FileType tex imap ,item \begin{itemize}<Enter><Tab>\item<space><Enter>\end{itemize}<Enter><Enter><++><Esc>3k5li<space>
autocmd FileType tex imap ,enum \begin{enumerate}<Enter><Tab>\item<space><Enter>\end{enumerate}<Enter><Enter><++><Esc>3k5li<space>
autocmd FileType tex imap ,listing \begin{lstlisting}<Enter>[caption=,<space>label=<++>]<Enter><++><Enter>\end{lstlisting}<Enter><Enter><++><Esc>4k6li
autocmd FileType tex imap ,v <ESC>:! xdg-open %<.pdf & <Enter>i
autocmd FileType tex imap ,c <ESC>:w! \| !pdflatex <c-r>%<CR>
autocmd FileType tex imap ,kursiv \textit{}<space><++><Esc>5hi
autocmd FileType tex imap ,fett \textbf{}<space><++><Esc>5hi
autocmd FileType tex imap ,quote \enquote{}<space><++><Esc>5hi
autocmd FileType tex imap ,sec \section{}<Enter><++><Esc>k6li
autocmd FileType tex imap ,ssec \subsection{}<Enter><++><Esc>k9li
autocmd FileType tex imap ,sssec \subsubsection{}<Enter><++><Esc>k12li
autocmd FileType tex imap ,par \paragraph{}<Enter><++><Esc>k8li
autocmd FileType tex imap ,ref \ref{}<space><++><Esc>5hi
autocmd FileType tex imap ,label \label{}<space><++><Esc>5hi
autocmd FileType tex imap ,bild \begin{figure}[h!]<Enter><Tab>\centering<Enter>\includegraphics[scale=]{<++>}<Enter>\caption{<++>}<Enter>\label{fig:<++>}<Enter><BS>\end{figure}<Enter><Enter><++><Esc>5k24li
autocmd FileType tex imap ,tikz \begin{figure}[h!]<Enter><Tab>\centering<Enter>\begin{tikz}<Enter><Tab><Enter><BS>\end{tikz}<Enter>\caption{<++>}<Enter>\label{fig:<++>}<Enter><BS>\end{figure}<Enter><Enter><++><Esc>6ki
autocmd FileType tex imap ,tabular \begin{tabular}{}<Enter><Tab><++><Enter><BS>\end{tabular}<Enter><Enter><++><Esc>4k13li
autocmd FileType tex imap ,table \begin{table}[h!]<Enter><Tab>\centering\begin{tabular}{}<Enter><Tab><++><Enter><BS>\end{tabular}<Enter>\caption{<++>}<Enter>\label{tab:<++>}<Enter><BS>\end{table}<Enter><Enter><++><Esc>7k17li
"compile file
autocmd FileType tex map ,c :w! \| !pdflatex <c-r>%<CR>
autocmd FileType tex map ,v :! xdg-open %<.pdf & <Enter>i
autocmd FileType tex imap ,cite \cite{} <++><Esc>5hi
autocmd FileType tex imap ,pack \usepackage{}<Enter><++><Esc>k9li
autocmd FileType tex imap ,packop \usepackage[]{<++>}<Enter><++><Esc>k15li


