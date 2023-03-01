#!/bin/bash

[[ $(echo $* | grep -c ".pdf") -eq 0 ]] && echo "Provide a pdf argument." && exit 1
[[ ! -f ${1%.pdf}.tex ]] && echo "${1%.pdf}.tex file not found" && exit 1

echo -e "\e[36;1mUse Ctrl+click in Zathura or ,r in vim to sync back and forth!\e[0m"

sleep 0.5

st -e bash -c "vim ${1%pdf}tex --servername $1" &

sleep 0.2

echo "vim --servername $1 --remote +%{line} %{input}"

zathura $1 -x "vim --servername $1 -c \"let g:syncpdf='$1'\" --remote +%{line} %{input}" &


ls *.tex *.sty | entr -rs "rm ${1%pdf}aux; timeout 10 pdflatex -synctex=1 --shell-escape ${1%pdf}tex"

#ls *.tex *.sty | entr -s "timeout 10 make"
