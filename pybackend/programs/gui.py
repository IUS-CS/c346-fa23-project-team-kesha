# importing required libraries
import tkinter as tk
from tkinter import *
import pygame
from videoDownload import Download



root = Tk()
root.title('Team Kesha Youtube Audio Player')

root.geometry("800x600")

pygame.mixer.init()  # initialise the pygame



def play(song_path):
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play(loops=0)

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()


# Text input


def download():
    link = txt0.get(1.0, "end-1c")
    name = txt1.get(1.0, "end-1c")
    audio_folder = "pybackend/MP3-Files/"
    song_name = Download(link, name)
    song_path = audio_folder + song_name
    play(song_path)




# Title Creation
title = Label(root, text="Youtube Audio Player", bd=9, relief=GROOVE,
              font=("Courier New", 50, "bold"), bg="white", fg="red")
title.pack(side=TOP, fill=X)


# TextBox Creation
l = Label(root, text = "Insert Youtube Link", font=("Courier New", 14))
txt0 = tk.Text(root, height = 2, width = 80)
l.pack()
txt0.pack()
L = Label(root, text = "Insert Song Name (No Spaces)",  font=("Courier New", 14))
txt1 = tk.Text(root, height = 2, width = 20)
L.pack()
txt1.pack()

# End text input

# Download and Play Button
play_button = Button(root, text="Play Song", font=("Courier New", 32), command=download)
play_button.pack(pady=10)
# End Download and Play

# Pause Button
# Need to add a statement to only show pause when music is playing
pause_button = Button(root, text="Pause", font=("Courier New", 32), command=pause)
pause_button.pack(pady=10)
# End Pause Button

# Unpause Button
# Need to add a statement to only show pause when music is paused
unpause_button = Button(root, text="Unpause", font=("Courier New", 32), command=unpause)
unpause_button.pack(pady=10)
# End Unpause Button

root.mainloop()