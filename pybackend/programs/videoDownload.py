from pytube import YouTube
import shutil
import os
import subprocess

name = "callher"
link = "https://youtu.be/IZBLdJB0TIE?si=8p-8jF5GoFiggO69"
destination = "pybackend/MP3-Files"

def Download(link, name):
    mp3_name = name + '.mp3'
    mp3_file_path = destination + "/" + mp3_name
    if os.path.exists(mp3_file_path):
        print("File already exists")
        return "N/A"
    else:
        youtubeObject = YouTube(link)
        youtubeObject = youtubeObject.streams.get_highest_resolution()
        try:
            source = youtubeObject.download()
            head, tail = os.path.split(f"{source}")
            subprocess.run(['ffmpeg -i "' + f"{tail}" +'" ' + mp3_name], shell=True)
            dest = shutil.move(mp3_name, destination)
            os.remove(source)
            print("Download Complete")
            return mp3_file_path
        except:
            print("An error has occurred")

