#!/bin/bash

# 
# Script that will take an input of a phrase from friends and open up the 
# episode in which the phrase was first said!
# 

cd
cd "$1"

echo -n "Enter keyword for Any episode of the show "
echo "Current directory: $(pwd)"
read text
echo "$text"
var=$(find . -name *.srt | xargs -d "\n" egrep -i '.*'"$text"'.*')
echo "$var" | cut -d ":" -f2 | head -1
file=$(echo "$var" | cut -d ":" -f1 | head -1 )
len="${#file}"
if [ "$len" == 0 ]
	then
	 	echo "no file found"
	else
		vlc  "${file%.*}.mkv"
fi
