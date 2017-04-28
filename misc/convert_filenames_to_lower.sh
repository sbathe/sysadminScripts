#!/bin/bash
# Convert filenames to lowercase
# and replace characters recursively
#####################################

if [ -z $1 ];then echo Give target directory; exit 0;fi

find "$1" -depth -name '*' | while read file ; do
        directory=$(dirname "$file")
        oldfilename=$(basename "$file")
	newfilename=$(echo "$oldfilename" | tr ' ' '_' | tr -d '[{}(),\!]' | tr -d "\'" | tr '[A-Z]' '[a-z]' | sed 's/_-_/_/g')
        if [ "$oldfilename" != "$newfilename" ]; then
                mv -i "$directory/$oldfilename" "$directory/$newfilename"
                echo ""$directory/$oldfilename" ---> "$directory/$newfilename""
                #echo "$directory"
                #echo "$oldfilename"
                #echo "$newfilename"
                #echo
        fi
        done
exit 0
