# YouTube Audio Player

An Audio Player application built using Python, Tkinter, and Pygame.

## Description

This application allows users to play and manage audio files in a designated playlist. It features a simple and intuitive user interface with play, pause, stop, skip, and repeat functionalities. Users can also select a folder containing audio files to create a playlist.

## Features

Play/Pause audio

Stop audio playback

Download audio from YouTube 

Skip to the next or previous track

Repeat playlist functionality

Progress bar to visualize playback progress

## Requirements

Python 3

Pygame library

Tkinter library

PyTube library

FFMpeg library

## Installation

1. Download the project
2. If you do not already have Python you can download it from [here](https://www.python.org/downloads/).
3. Open a terminal and navigate to the project folder<br>
    <code>$ cd (project directory)</code>
5. Install pygame by running the below<br>
   <code>$ python -m pip install pygame</code>
6. Install tkinter by running the below<br>
   <code>$ python -m pip install tk</code>
7. Install FFMpeg by running the below<br>
    <code>$ python -m pip install ffmpeg</code> (Recommend running with brew <code>$ brew install ffmpeg</code>)
8. Install PyTube by running the below<br>
    <code>$ python -m pip install pytube</code>

   (If pip is outdated, install from the source: <code>$ python -m pip install git+https://github.com/pytube/pytube</code>)

## Running the application

To run the application you can use the following:<br>
<code>$ python gui2.py</code>

Select a playlist using the button located in the top right.<br>
![Image](doc/Images/select_playlist.png)

Control audio playback using the provided buttons (play, pause, stop, skip, repeat).
