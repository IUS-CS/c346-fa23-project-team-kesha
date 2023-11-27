from pytube import YouTube
import shutil
import os
import subprocess

audio_folder = "pybackend/MP3-Files"

def create_new_playlist(playlist_name):
    if not os.path.exists(audio_folder + "/" + f"{playlist_name}"):
        try:
            os.makedirs(audio_folder + "/" + f"{playlist_name}")
            print("Playlist Created")
        except:
            print("Playlist could not be created")
    else:
        print("Playlist already exists")


def remove_playlist(playlist_name):
    if os.path.exists(audio_folder + "/" + f"{playlist_name}"):
        try:
            shutil.rmtree(audio_folder + "/" + f"{playlist_name}")
            print("Playlist Deleted")
        except:
            print("Playlist could not be deleted")
    else:
        print("Playlist does not exist")



def Download(link, name):
    mp3_name = name + '.mp3'
    mp3_file_path = audio_folder + "/" + mp3_name
    if os.path.exists(mp3_file_path):
        print("File already exists")
        return mp3_name
    else:
        youtubeObject = YouTube(link)
        youtubeObject = youtubeObject.streams.get_highest_resolution()
        try:
            source = youtubeObject.download()
            head, tail = os.path.split(f"{source}")
            subprocess.run(['ffmpeg -i "' + f"{tail}" +'" ' + mp3_name], shell=True)
            dest = shutil.move(mp3_name, audio_folder)
            os.remove(source)
            print("Download Complete")
            return mp3_name
        except:
            print("An error has occurred")


# List the songs
def show_songs(playlist):
    dir_list = os.listdir(audio_folder + playlist + "/")

    x = 0

    for split in dir_list:
        split_list = split.split(".")
        dir_list[x] = split_list[0]
        x += 1

    print(dir_list)

def show_playlists():
    dir_list = os.listdir(audio_folder + "/")

    x = 0

    for split in dir_list:
        split_list = split.split(".")
        dir_list[x] = split_list[0]
        x += 1

    print(dir_list)

Download("https://youtu.be/5yIbZVOv438?si=yFjlD0qNSY2HKhRT", "Earth")