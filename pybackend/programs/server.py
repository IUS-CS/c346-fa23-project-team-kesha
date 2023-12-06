#File to listen to server and call functions to add files to database from a youtube url
import pymongo
from pymongo import MongoClient
import gridfs
import sys
import socket
from bson.objectid import ObjectId
from file_manipulation import Download

 

#Define Globals
client = MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000")
db = client.playlist

#Create Instance of GridFS
fs = gridfs.GridFS(db)
#Insert File Definition from GridFS
#Get File Definition from GridFS

def insert_song(file_path):
    
    with open(file_path, 'rb') as f:
        song_id = fs.put(f.read())
        print([p for p in db.fs.files.find({"_id": ObjectId(song_id)})])



# name = input("Enter the name of your song: ")
# link = input("Enter the YouTube video URL: ")
# song_path = input("Enter Path")
song_path = "/Users/noahtrejo/MP3-FIles"
song = Download("https://youtu.be/5yIbZVOv438?si=yFjlD0qNSY2HKhRT", "Earth", "/Users/noahtrejo/MP3-FIles")
if song == "N/A":
    print("Song already in playlist")
else:
    insert_song(song_path + "/" + song)
    print("File downloaded and stored in playlists")