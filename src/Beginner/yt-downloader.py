### Youtube MP3 Downloader ###
# This script will download the audio from a YouTube video and save it as an MP3 file.
# The user is prompted to enter a YouTube video URL and select a folder to save the MP3 file to
# The script will then download the audio and save it as an MP3 file in the selected folder

import os
import re
from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def clean_filename(filename):
    invalid_chars = re.compile(r'[\\/:"*?<>|]')  # Add any other characters that are invalid on your system
    cleaned_filename = re.sub(invalid_chars, '', filename)
    
    return cleaned_filename

def download_audio(url, save_path):
    try:
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        temp_filename = os.path.join(save_path, audio_stream.default_filename)
        audio_stream.download(output_path=save_path)

        new_title = clean_filename(yt.title)
        new_filename = os.path.join(save_path, f"{new_title}.mp3")
        os.rename(temp_filename, new_filename)
        print(f"Audio downloaded successfully as {new_filename}")
    except Exception as e:
        print(e)

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")
    return folder

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    video_url = input("Please enter the video URL of the video you are wanting to download. ")
    save_path = open_file_dialog()

    if not save_path:
        print("Invalid save path! Please select a valid location.")
    else:
        download_audio(video_url, save_path)
