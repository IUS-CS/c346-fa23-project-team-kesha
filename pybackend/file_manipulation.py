from pytube import YouTube
import shutil
import os
import subprocess

audio_folder = "pybackend/MP3-Files"

def create_new_playlist(path, playlist_name):
    if not os.path.exists(path + "/" + f"{playlist_name}"):
        try:
            os.makedirs(path + "/" + f"{playlist_name}")
            print("Playlist Created")
        except:
            print("Playlist could not be created")
    else:
        print("Playlist already exists")


def remove_playlist(path, playlist_name):
    if os.path.exists(path + "/" + f"{playlist_name}"):
        try:
            shutil.rmtree(path + "/" + f"{playlist_name}")
            print("Playlist Deleted")
        except:
            print("Playlist could not be deleted")
    else:
        print("Playlist does not exist")



def Download(link, name, path):
    mp3_name = name + '.mp3'
    mp3_file_path = path + "/" + mp3_name
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
            dest = shutil.move(mp3_name, path)
            os.remove(source)
            print("Download Complete")
            return mp3_name
        except:
            print("An error has occurred")


# List the songs
def show_songs(path, playlist):
    dir_list = os.listdir(path + playlist + "/")

    x = 0

    for split in dir_list:
        split_list = split.split(".")
        dir_list[x] = split_list[0]
        x += 1

    print(dir_list)

def show_playlists(path):
    dir_list = os.listdir(path + "/")

    x = 0

    for split in dir_list:
        split_list = split.split(".")
        dir_list[x] = split_list[0]
        x += 1

    print(dir_list)
# create_new_playlist("/Users/noahtrejo", "MP3-Files")

# Download("https://youtu.be/5yIbZVOv438?si=yFjlD0qNSY2HKhRT", "Earth", "/Users/noahtrejo/MP3-FIles")
# Download("https://youtu.be/Q2-WKpaHsdM?si=4ySh2WV5kVaWpflE", "Secrets", "/Users/noahtrejo/MP3-FIles")

# remove_playlist("/Users/noahtrejo", "MP3-Files")