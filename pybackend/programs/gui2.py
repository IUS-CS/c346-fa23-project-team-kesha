import os
import pygame
from tkinter import Tk, Frame, Button, Label, filedialog, ttk, PhotoImage

class AudioPlayer:
    def __init__(self, master):
        self.master = master
        master.title("Audio Player")
        master.geometry("800x600")

        self.current_file = None
        self.paused = False
        self.audio_folder_path = None
        self.playlist_path = None
        self.playlist = []

        # Load button images
        self.play_image = PhotoImage(
            file="doc/Images/play.png").subsample(40,40)  # Change "path_to_play_image.png" to the actual path of your play button image
        self.stop_image = PhotoImage(
            file="doc/Images/stop.png").subsample(6,6)  # Change "path_to_stop_image.png" to the actual path of your stop button image
        self.skip_image = PhotoImage(
            file="doc/Images/skip.png").subsample(6,6)  # Change "path_to_skip_image.png" to the actual path of your skip button image
        self.play_all_image = PhotoImage(
            file="doc/Images/repeat.png").subsample(20,20)  # Change "path_to_play_all_image.png" to the actual path of your play all button image
        self.previous_image = PhotoImage(
            file="doc/Images/previous.png").subsample(7,7)  # Change "path_to_play_all_image.png" to the actual path of your play all button image
        self.select_folder_image = PhotoImage(
            file="doc/Images/select_playlist.png").subsample(2,2)  # Change "path_to_play_all_image.png" to the actual path of your play all button image
        self.pause_image = PhotoImage(
            file="doc/Images/pause.png").subsample(6,6)  # Change "path_to_play_all_image.png" to the actual path of your play all button image

        pygame.mixer.init()

        self.setup_gui()

    def setup_gui(self):
        self.label = Label(self.master, text="Select A Playlist")
        self.label.pack(padx=5, pady=5, side="top", anchor="ne")

        self.select_folder_button = Button(self.master, image=self.select_folder_image, command=self.select_folder)
        self.select_folder_button.pack(padx=15, pady=5, side="right", anchor="ne")

        self.folder_label = Label(self.master, text="Selected Playlist: None", font=("Helvetica", 16, "bold"))
        self.folder_label.pack(padx=1, pady=1, side="top", anchor="nw")

        self.progress_bar = ttk.Progressbar(self.master, orient="horizontal", mode="determinate", length=400)
        self.progress_bar.pack(pady=5)

        self.play_button = Button(self.master, image=self.play_image, command=self.play_pause)
        self.play_button.pack(pady=5)

        self.stop_button = Button(self.master, image=self.stop_image, command=self.stop)
        self.stop_button.pack(pady=5)

        self.skip_button = Button(self.master, image=self.skip_image, command=self.play_next)
        self.skip_button.pack(pady=5)

        self.play_all_button = Button(self.master, image=self.play_all_image, command=self.play_all)
        self.play_all_button.pack(pady=5)

        self.previous_button = Button(self.master, image=self.previous_image, command=self.play_previous)
        self.previous_button.pack(pady=5)

        # Center the buttons at the bottom
        self.play_all_button.place(relx=0.2, rely=0.97, anchor="s")
        self.previous_button.place(relx=0.4, rely=0.97, anchor="s")
        self.play_button.place(relx=0.5, rely=0.97, anchor="s")
        self.skip_button.place(relx=0.6, rely=0.97, anchor="s")
        self.stop_button.place(relx=0.8, rely=0.97, anchor="s")

        # Position the progress bar above the bottom buttons
        self.progress_bar.place(relx=0.5, rely=0.92, anchor="s")

        self.audio_buttons_frame = Frame(self.master)
        self.audio_buttons_frame.pack(side="left", padx=10, pady=10, anchor="nw")

        self.audio_buttons = []

        self.update_audio_buttons()

        self.update_progress()

    def update_audio_buttons(self):
        # Clear existing buttons
        for button in self.audio_buttons:
            button.destroy()

        if self.audio_folder_path:
            audio_files = [file for file in os.listdir(self.audio_folder_path) if file.endswith(".mp3")]

            for audio_file in audio_files:
                button = Button(self.audio_buttons_frame, text=audio_file, command=lambda f=audio_file: self.select_audio_from_button(f))
                button.pack(pady=5)
                self.audio_buttons.append(button)

            self.playlist = [os.path.join(self.audio_folder_path, file) for file in audio_files]

    def select_folder(self):
        folder_path = filedialog.askdirectory(title='Select Folder to Play From')  # shows dialog box and returns the path

        if folder_path:
            self.audio_folder_path = folder_path
            self.folder_label.config(text=f"{os.path.basename(folder_path)}")
            self.update_audio_buttons()

    def select_audio_from_button(self, audio_file):
        self.current_file = os.path.join(self.audio_folder_path, audio_file)
        self.label.config(text=os.path.basename(self.current_file))
        self.progress_bar["value"] = 0  # Reset progress bar when a new file is selected

    def play_all(self):
        if self.playlist:
            self.current_file = self.playlist[0]
            self.label.config(text=os.path.basename(self.current_file))
            pygame.mixer.music.load(self.current_file)
            pygame.mixer.music.play()
            self.play_button.config(image=self.pause_image)

    def update_progress(self):
        if pygame.mixer.music.get_busy() and not self.paused:
            current_time = pygame.mixer.music.get_pos() / 1000  # in seconds
            total_time = pygame.mixer.Sound(self.current_file).get_length()

            progress_percentage = (current_time / total_time) * 100
            self.progress_bar["value"] = progress_percentage

            # Check if the song has ended, then play the next one in the playlist
            if progress_percentage >= 100:
                self.play_next()

        self.master.after(10000, self.update_progress)

    def play_next(self):
        if self.playlist:
            index = self.playlist.index(self.current_file)
            next_index = (index + 1) % len(self.playlist)
            self.current_file = self.playlist[next_index]
            self.label.config(text=os.path.basename(self.current_file))
            pygame.mixer.music.load(self.current_file)
            pygame.mixer.music.play()

    def play_previous(self):
        if self.playlist:
            index = self.playlist.index(self.current_file)
            previous_index = (index - 1) % len(self.playlist)
            self.current_file = self.playlist[previous_index]
            self.label.config(text=os.path.basename(self.current_file))
            pygame.mixer.music.load(self.current_file)
            pygame.mixer.music.play()

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

    def stop(self):
        pygame.mixer.music.stop()
        self.play_button.config(text="Play")
        self.paused = False

if __name__ == "__main__":
    root = Tk()
    audio_player = AudioPlayer(root)
    root.mainloop()
