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
var=$(grep -B 2 --include=\*.{srt,} -rnw "$(pwd)" -ie  '.*'"$text"'.*')




line=$(echo "$var" | head -3)
file=$(echo "$line" |  tail -1 | cut -d ":" -f1)

len="${#file}"
if [ "$len" == 0 ]
	then
	 	echo "no file found"
	else
		echo "$file"
		t=$(echo "$line" | head -2)
		time_to_start=""
		first=$(echo "$t"| head -1 | awk -F ".srt" '{print $2}' | awk -F "[0-9]+-" '{print $2}' | awk -F " --> " '{print $2}' | cut -d "," -f1)
		if [ "$first" == "" ]
			then
				second=$(echo "$t"| tail -1 | awk -F ".srt" '{print $2}' | awk -F "[0-9]+-" '{print $2}'| awk -F " --> " '{print $2}' | cut -d "," -f1)
				time_to_start=$second
			else
				time_to_start=$first

		fi
		echo "$time_to_start"
		seconds=$(echo "$time_to_start" | awk -F: '{ print ($1 * 3600) + ($2 * 60) + $3 - 5}')
		vlc  "${file%.*}.mkv" --start-time="$seconds"
		#echo "${file%.*}.mkv"
fi

#vlc filename --start-time=time in secs
