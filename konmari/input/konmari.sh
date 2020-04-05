#!/bin/bash

#ext_compressed="*+(.zip|.tar.gz|.tar|.rar)" #add what you want
#ext_docs="*+(.doc|.docx|.ppt|.pptx|.pdf)" #add what you want
#ext_img="*+(.jpg|.png|.gif)" #add what you want
#ext_musics= "*+(.mp3|.flac|.aac)"#add what you want
#ext_program="*+(.deb|.exe|.cpp|.py|.html|.css|.js|.sh|.ps1)" #add what you want
#ext_video="*+(.mp4|.mkv|.flv)"  #add what you want

do
then
		mkdir -p Compressed
		mv "*+(.zip|.tar.gz|.tar|.rar)" Compressed
done
do
then
		mkdir -p Documents
		mv "*+(.doc|.docx|.ppt|.pptx|.pdf)" Documents
done

#	elif [ $folder == 'Images' ]
#	then
#		mkdir -p $folder
#		mv $ext_img /Images
#
#	elif [ $folder == 'Music' ]
#	then
#		mkdir -p $folder
#		mv $ext_musics /Music
#
#	elif [ $folder == 'Programs' ]
#	then
#		mkdir -p $folder
#		mv $ext_program /Programs
	
#	elif [ $folder == 'Videos' ]
#	then
#		mkdir -p $folder
#		mv $ext_video /Videos

#	else
#		echo "Passing other files"
#	fi

#done

echo "Decluterred with Konmari method"

