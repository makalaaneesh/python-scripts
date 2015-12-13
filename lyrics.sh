#!/bin/bash

# A script that will fetch lyrics with file as argument 
# requires mp3info Run sudo-apt get install mp3info if not installed

artist=$(mp3info -p %a "$1")
title=$(mp3info -p %t "$1")
echo "aritst is $artist and title is $title"
vlc -vvv "$1"&
python lyrics.py "$title" "|" "$artist" 