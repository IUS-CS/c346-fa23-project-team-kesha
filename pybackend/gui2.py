# GUI for the AudioPlayer
# Uses the download feature from backend to download links

import os
import tkinter

import pygame
from tkinter import *
from tkinter import Tk, Frame, Button, Label, filedialog, ttk, PhotoImage, Text
# import threading
from file_manipulation import Download
from PIL import Image, ImageTk


class AudioPlayer:
    # Initialize the GUI
    def __init__(self, master):
        self.master = master
        master.title("Audio Player")
        master.geometry("800x600")

        self.current_file = None
        self.paused = False
        self.audio_folder_path = None
        self.playlist_path = None
        self.playlist = []

        # Label Definitions
        self.label = None
        self.folder_label = None
        self.link_label = None

        # Button Definitions
        self.download_button = None
        self.select_folder_button = None
        self.play_button = None
        self.stop_button = None
        self.skip_button = None
        self.play_all_button = None
        self.previous_button = None
        self.back_button = None
        self.audio_buttons = None

        # Text Definitions
        self.link_text = None
        self.name_text = None

        # Progress Bar Definition
        self.progress_bar = None

        # Frame Definitions
        self.audio_buttons_frame = None

        # Load button images
        self.play_image = PhotoImage(
            file="doc/Images/play.png").subsample(40, 40)
        self.stop_image = PhotoImage(
            file="doc/Images/stop.png").subsample(6, 6)
        self.skip_image = PhotoImage(
            file="doc/Images/skip.png").subsample(6, 6)
        self.play_all_image = PhotoImage(
            file="doc/Images/repeat.png").subsample(20, 20)
        self.previous_image = PhotoImage(
            file="doc/Images/previous.png").subsample(7, 7)
        self.select_folder_image = PhotoImage(
            file="doc/Images/select_playlist.png").subsample(2, 2)
        self.pause_image = PhotoImage(
            file="doc/Images/pause.png").subsample(6, 6)
        self.download_image = PhotoImage(
            file="doc/Images/download.png").subsample(5, 5)

        pygame.mixer.init()
        # Set up the front page buttons and labels
        self.setup_gui()

    def setup_gui(self):

        # Labels
        self.label = Label(self.master, text="Select A Playlist")

        self.folder_label = Label(self.master, text=" ", font=("Helvetica", 16, "bold"))

        self.link_label = Label(self.master, text="Add Song", font=("Courier New", 14))

        # Buttons

        self.back_button = Button(self.master, text="Back", command=self.unpack_all)

        self.download_button = Button(self.master, image=self.download_image, command=self.download)

        self.select_folder_button = Button(self.master, image=self.select_folder_image, command=self.select_folder)

        self.play_button = Button(self.master, image=self.play_image, command=self.play_pause)

        self.stop_button = Button(self.master, image=self.stop_image, command=self.stop)

        self.skip_button = Button(self.master, image=self.skip_image, command=self.play_next)

        self.play_all_button = Button(self.master, image=self.play_all_image, command=self.play_all)

        self.previous_button = Button(self.master, image=self.previous_image, command=self.play_previous)

        # Text
        self.link_text = Text(self.master, width=50, height=1)
        self.name_text = Text(self.master, width=20, height=1)

        # Progress Bar
        self.progress_bar = ttk.Progressbar(self.master, orient="horizontal", mode="determinate", length=400)

        # Initial Packing
        self.label.pack(padx=5, pady=5, side="top", anchor="ne")
        self.folder_label.pack(padx=1, pady=1, side="top", anchor="nw")
        self.select_folder_button.pack(padx=15, pady=5, side="right", anchor="ne")

        self.audio_buttons_frame = Frame(self.master)
        self.audio_buttons_frame.pack(side="left", padx=10, pady=10, anchor="nw")

        self.audio_buttons = []

        self.update_audio_buttons()

        # threading.Thread(target=self.update_progress).start()

    def initial_unpack(self):
        self.select_folder_button.place_forget()
        self.select_folder_button.pack_forget()
        self.label.place_forget()
        self.label.pack_forget()

    def unpack_all(self):

        # Delete Text
        self.link_text.delete(1.0, "end")
        self.name_text.delete(1.0, "end")

        # Initial Un-Placing
        self.play_button.place_forget()
        self.stop_button.place_forget()
        self.skip_button.place_forget()
        self.play_all_button.place_forget()
        self.previous_button.place_forget()
        self.progress_bar.place_forget()
        self.back_button.place_forget()
        self.link_text.place_forget()
        self.name_text.place_forget()
        self.download_button.place_forget()
        self.folder_label.place_forget()
        self.link_label.place_forget()

        # Initial unpacking
        self.play_button.pack_forget()
        self.stop_button.pack_forget()
        self.skip_button.pack_forget()
        self.play_all_button.pack_forget()
        self.previous_button.pack_forget()
        self.progress_bar.pack_forget()
        self.back_button.pack_forget()
        self.link_text.pack_forget()
        self.name_text.pack_forget()
        self.download_button.pack_forget()
        self.folder_label.pack_forget()
        self.link_label.pack_forget()

        # Clear Existing Audio Buttons
        for button in self.audio_buttons:
            button.destroy()

        # Initial Packing
        self.label.pack(padx=5, pady=5, side="top", anchor="ne")
        self.select_folder_button.pack(padx=15, pady=5, side="right", anchor="ne")

    def update_player_buttons(self):

        # Initial Packing
        self.back_button.pack(pady=1, padx=0)
        self.play_button.pack(pady=5)
        self.stop_button.pack(pady=5)
        self.skip_button.pack(pady=5)
        self.play_all_button.pack(pady=5)
        self.previous_button.pack(pady=5)
        self.progress_bar.pack(pady=5)
        self.folder_label.pack(padx=1, pady=1)

        # Center the buttons at the bottom
        self.back_button.place(relx=0, rely=1.0, anchor="sw")
        self.folder_label.place(relx=1.0, rely=0, anchor="ne")
        self.play_all_button.place(relx=0.2, rely=0.97, anchor="s")
        self.previous_button.place(relx=0.4, rely=0.97, anchor="s")
        self.play_button.place(relx=0.5, rely=0.97, anchor="s")
        self.skip_button.place(relx=0.6, rely=0.97, anchor="s")
        self.stop_button.place(relx=0.8, rely=0.97, anchor="s")

        # Position the progress bar above the bottom buttons
        self.progress_bar.place(relx=0.5, rely=0.92, anchor="s")

        # Bind Placeholder Events

        self.link_text.bind("<FocusIn>", self.link_on_entry_click)
        self.link_text.bind("<FocusOut>", self.link_on_focus_out)

        self.name_text.bind("<FocusIn>", self.name_on_entry_click)
        self.name_text.bind("<FocusOut>", self.name_on_focus_out)

    def update_audio_buttons(self):
        # Clear existing buttons
        for button in self.audio_buttons:
            button.destroy()

        if self.audio_folder_path:
            audio_files = [file for file in os.listdir(self.audio_folder_path) if file.endswith(".mp3")]

            for audio_file in audio_files:
                button = Button(self.audio_buttons_frame,
                                text=audio_file.split(".")[0],
                                command=lambda f=audio_file: self.select_audio_from_button(f)
                                )
                button.pack(padx=1, pady=3)
                self.audio_buttons.append(button)

            self.playlist = [os.path.join(self.audio_folder_path, file) for file in audio_files]

    def update_text_box(self):
        self.link_label.pack(anchor="n", padx=1, pady=2)
        self.link_text.pack(anchor="n", padx=1, pady=2)
        self.name_text.pack(anchor="n", padx=1, pady=2)
        self.download_button.pack(anchor="n", padx=1, pady=2)
        self.link_text.insert(INSERT, "Enter Link")
        self.name_text.insert(INSERT, "Enter Song Name")

    # Shows dialog box and returns the path
    def select_folder(self):

        folder_path = filedialog.askdirectory(title='Select Folder to Play From')

        if folder_path:
            self.audio_folder_path = folder_path
            self.folder_label.config(text=f"{os.path.basename(folder_path)}")
            self.update_audio_buttons()
            self.update_player_buttons()
            self.playlist_path = folder_path
            self.update_text_box()
            self.initial_unpack()

    # Selecting a song to play
    def select_audio_from_button(self, audio_file):
        self.current_file = os.path.join(self.audio_folder_path, audio_file)
        self.label.config(text=os.path.basename(self.current_file))
        self.progress_bar["value"] = 0  # Reset progress bar when a new file is selected

    # Play all contents of a folder
    def play_all(self):
        if self.playlist:
            self.current_file = self.playlist[0]
            self.label.config(text=os.path.basename(self.current_file))
            pygame.mixer.music.load(self.current_file)
            pygame.mixer.music.play()
            self.play_button.config(image=self.pause_image)

    # Update the progress bar recursively
    def update_progress(self):
        if pygame.mixer.music.get_busy() and not self.paused:
            current_time = pygame.mixer.music.get_pos() / 1000  # in seconds
            total_time = pygame.mixer.Sound(self.current_file).get_length()

            progress_percentage = (current_time / total_time) * 100
            self.progress_bar["value"] = progress_percentage

            # Check if the song has ended, then play the next one in the playlist
            if progress_percentage >= 100:
                self.play_next()

        self.master.after(100, self.update_progress)

    # Play the next song in the folder
    def play_next(self):
        if self.playlist:
            index = self.playlist.index(self.current_file)
            next_index = (index + 1) % len(self.playlist)
            self.current_file = self.playlist[next_index]
            self.label.config(text=os.path.basename(self.current_file))
            pygame.mixer.music.load(self.current_file)
            pygame.mixer.music.play()

    # Play the previous song in the folder
    def play_previous(self):
        if self.playlist:
            index = self.playlist.index(self.current_file)
            previous_index = (index - 1) % len(self.playlist)
            self.current_file = self.playlist[previous_index]
            self.label.config(text=os.path.basename(self.current_file))
            pygame.mixer.music.load(self.current_file)
            pygame.mixer.music.play()

    # Play(if the music is paused) or Pause(if the music is playing) the music
    def play_pause(self):
        if self.current_file:
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.load(self.current_file)
                pygame.mixer.music.play()
                self.play_button.config(image=self.pause_image)
            else:
                if self.paused:
                    pygame.mixer.music.unpause()
                    self.paused = False
                    self.play_button.config(image=self.pause_image)
                else:
                    pygame.mixer.music.pause()
                    self.paused = True
                    self.play_button.config(image=self.play_image)

    # Stop the music playback
    def stop(self):
        pygame.mixer.music.stop()
        self.play_button.config(image=self.play_image)
        self.paused = True

    # Download a song into the current playlist based on the link provided
    def download(self):
        Download(
            self.link_text.get(1.0, "end-1c"),
            self.name_text.get(1.0, "end-1c"),
            self.playlist_path
        )
        self.update_audio_buttons()

    def link_on_entry_click(self, event):
        if self.link_text.get(1.0, "end-1c") == "Enter Link":
            self.link_text.delete(1.0, "end-1c")

    def link_on_focus_out(self, event):
        if self.link_text.get(1.0, "end-1c") == "":
            self.link_text.insert(1.0, "Enter Link")

    def name_on_entry_click(self, event):
        if self.name_text.get(1.0, "end-1c") == "Enter Song Name":
            self.name_text.delete(1.0, "end-1c")

    def name_on_focus_out(self, event):
        if self.name_text.get(1.0, "end-1c") == "":
            self.name_text.insert(1.0, "Enter Song Name")


if __name__ == "__main__":
    root = Tk()
    audio_player = AudioPlayer(root)



    root.mainloop()
