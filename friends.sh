#!/bin/bash
#creating the link
sudo ln -s /media/makala/WINDOWS/Users/user/Downloads/Friends\ Complete\ Seasons\ 1-10\ Uncut\ DVDRip\ -\ 480p/ 

#cd into a random directory
cd Friends\ Complete\ Seasons\ 1-10\ Uncut\ DVDRip\ -\ 480p
dirs=(*/) #storing all the directories in the pwd into dirs
N=${#dirs[@]}           # Number of members in the array
((N=RANDOM%N)) #random
randomdir=${dirs[$N]} #storing the path in randomfile
echo $randomdir
cd "$randomdir"

#vlc open a random file
files=(*.mkv)
N=${#files[@]}  
((N=RANDOM%N))
randomfile=${files[$N]}
echo $randomfile
vlc "$randomfile"

