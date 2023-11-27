# importing required libraries
import os
import tkinter as tk
from tkinter import *
import pygame
from file_manipulation import Download, create_new_playlist, remove_playlist, show_songs, show_playlists

audio_folder = os.path.dirname(os.path.abspath(__file__))
root = Tk()
root.title('Team Kesha Youtube Audio Player')
root.geometry("800x600")

pygame.mixer.init()  # initialize the pygame

# Play Function
def play():
    show_pause_unpause_button()
    song_name = txt1.get(1.0, "end-1c")
    playlist = txt2.get(1.0, "end-1c")
    pygame.mixer.music.load(audio_folder + "" + f"{playlist}" + "" + f"{song_name}" + ".mp3")
    pygame.mixer.music.play(loops=0)


# Pause Function
def pause_unpause():
    if pygame.mixer.music.get_busy():
        pause_unpause_button['text'] = "⏸️"
        pygame.mixer.music.pause()
    else:
        pause_unpause_button['text'] = "▶️"
        pygame.mixer.music.play(loops=0)

# Unpause Function
# def unpause():
#     pygame.mixer.music.unpause()

# Download Function - downloads into audio_folder initially
def download():
    link = txt0.get(1.0, "end-1c")
    name = txt1.get(1.0, "end-1c")
    playlist = txt2.get(1.0, "end-1c")
    song_name = Download(link, f"{name}", playlist)

# Give the Current Playlist
def show_current_playlist():
    folder_path_list = audio_folder.split("/")
    playlist = folder_path_list[len(folder_path_list) - 2]
    playlist_label = Label(root, text="Playlist:\n" + playlist, font=("Courier New", 18))
    playlist_label.pack(pady=10)




# Title Creation
title = Label(root, text="Youtube Audio Player", bd=9, relief=GROOVE,
              font=("Courier New", 50, "bold"), bg="white", fg="red")
title.pack(side=TOP, fill=X)


# TextBox Creation
link_label = Label(root, text = "Insert Youtube Link", font=("Courier New", 14))
txt0 = tk.Text(root, height = 1, width = 40)
link_label.pack()
txt0.pack()

L = Label(root, text = "Insert Song Name(No spaces)",  font=("Courier New", 14))
txt1 = tk.Text(root, height = 1, width = 20)
L.pack()
txt1.pack()


playlist_label = Label(root, text = "Playlist to Add",  font=("Courier New", 14))
txt2 = tk.Text(root, height = 1, width = 20)
playlist_label.pack()
txt2.pack()
# End textbox creation

def show_download_button():
    # Download Button

    download_button.pack(pady=10)
    # End Download
def show_play_button():
    # Play Button

    play_button.pack(pady=10)
    # End Play

def show_pause_unpause_button():
    # Pause Button
    # Need to add a statement to only show pause when music is playing

    pause_unpause_button.pack(pady=10)
    # End Pause Button

# def show_unpause_button():
#     # Unpause Button
#     # Need to add a statement to only show pause when music is paused
#     unpause_button.pack(pady=10)
#     # End Unpause Button



def show_music_buttons():
    show_pause_unpause_button()
    # show_unpause_button()
def remove_music_buttons():
    pause_unpause_button.pack_forget()
    # unpause_button.pack_forget()




# Switch Playlist button DO THIS WILL LIST PLAYLIST AS WELL AND SONGS IN PLAYLIST
# FUNTION TO MAKE NEW PLAYLIST IS DOES NOT ALREADY EXIST
# FUNCTION TO ADD SONG TO PLAYLIST FROM MP3 FILES IF SONG EXISTS THERE
download_button = Button(root, text="Download Song", font=("Courier New", 32), command=download)
play_button = Button(root, text="Play Song", font=("Courier New", 32), command=play)
pause_unpause_button = Button(root, text="⏸️", font=("Courier New", 32), command=pause_unpause)
# unpause_button = Button(root, text="Unpause", font=("Courier New", 32), command=unpause)

show_download_button()
show_play_button()


root.mainloop()