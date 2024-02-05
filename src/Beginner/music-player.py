### Music Player ###
# Creates a music player that allows you to play, pause, stop, skip forward, skip backward, and shuffle songs.
# The program uses the pygame library to play music and the tkinter library to create the GUI.
# The playlist is stored in a file called playlist.txt, and the program allows you to add music to the playlist.
# The program also displays the current song being played and allows you to adjust the volume.
# Note: This program requires the pygame library to be installed. You can install it using pip: pip install pygame.

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pygame
import os
import random
import sys

class MusicPlayer:
    def __init__(self, master):
        self.master = master
        master.title("Music Player")

        self.playlist = []
        self.current_index = 0
        self.shuffle_mode = False
        self.played_songs = set() 

        self.load_playlist()

        self.play_button = tk.Button(master, text="Play", command=self.play)
        self.play_button.pack()

        self.pause_button = tk.Button(master, text="Pause", command=self.pause)
        self.pause_button.pack()

        self.stop_button = tk.Button(master, text="Stop", command=self.stop)
        self.stop_button.pack()

        self.skip_forward_button = tk.Button(master, text="Skip Forward", command=self.skip_forward)
        self.skip_forward_button.pack()

        self.skip_back_button = tk.Button(master, text="Skip Backward", command=self.skip_backward)
        self.skip_back_button.pack()

        self.shuffle_button = tk.Button(master, text="Shuffle", command=self.toggle_shuffle)
        self.shuffle_button.pack()

        self.volume_slider = ttk.Scale(master, from_=0, to=1, orient=tk.HORIZONTAL, command=self.set_volume)
        self.volume_slider.pack()
        self.volume_slider.set(0.5)

        self.add_button = tk.Button(master, text="Add Music", command=self.add_music)
        self.add_button.pack()

        self.shuffle_icon = tk.Label(master, text="🔀", font=("Arial", 12))  # Shuffle icon
        self.shuffle_icon.pack()

        self.current_song_label = tk.Label(master, text="Current Song: None")
        self.current_song_label.pack()

    def load_playlist(self):
        if os.path.exists("playlist.txt"):
            with open("playlist.txt", "r") as file:
                self.playlist = [line.strip() for line in file.readlines()]
        else:
            with open("playlist.txt", "w") as file:
                file.write("")
            self.playlist = []

    def save_playlist(self):
        try:
            with open("playlist.txt", "w") as file:
                for song in self.playlist:
                    file.write(song + "\n")
        except Exception as e:
            print("Error saving playlist:", e)

    def exit(self):
        pygame.mixer.music.stop()
        pygame.quit()
        self.save_playlist()
        self.master.quit()
        sys.exit()

    def play(self):
        if not self.playlist:
            messagebox.showinfo("No Music", "No music in playlist!")
            return

        if self.shuffle_mode:
            random.shuffle(self.playlist)

        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()

        if len(self.playlist) == len(set(self.playlist)):
            self.played_songs = set()

        remaining_songs = set(self.playlist) - self.played_songs
        if remaining_songs:
            new_song = random.choice(list(remaining_songs))
            self.played_songs.add(new_song)
            self.current_index = self.playlist.index(new_song)
        else:
            self.played_songs = set(self.playlist)

        song_path = self.playlist[self.current_index]
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play()
        self.update_current_song_label(os.path.basename(song_path))

    def stop(self):
        pygame.mixer.music.stop()

    def pause(self):
        pygame.mixer.music.pause()

    def skip_forward(self):
        if not self.playlist:
            return
        
        self.current_index += 1
        if self.current_index >= len(self.playlist):
            self.current_index = 0
        self.play()

    def skip_backward(self):
        if not self.playlist:
            return
        
        self.current_index -= 1
        if self.current_index < 0:
            self.current_index = len(self.playlist) - 1
        self.play()

    def toggle_shuffle(self):
        self.shuffle_mode = not self.shuffle_mode
        if self.shuffle_mode:
            random.shuffle(self.playlist)
            self.shuffle_icon.config(text="🔀")
        else:
            self.shuffle_icon.config(text="")

    def set_volume(self, volume):
        pygame.mixer.music.set_volume(float(volume))

    def add_music(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav;*.ogg;*.flac;*.aac")])
        if file_path:
            self.playlist.append(file_path)
            self.save_playlist() 
            print("Added:", os.path.basename(file_path))


    def update_current_song_label(self, song_name):
        self.current_song_label.config(text=f"Current Song: {song_name}")

    def show_playlist(self):
        playlist_window = tk.Toplevel(self.master)
        playlist_window.title("Playlist")

        def delete_song(index):
            del self.playlist[index]
            self.save_playlist()
            playlist_window.destroy()
            self.show_playlist()

        if self.playlist:
            for i, song in enumerate(self.playlist):
                song_frame = tk.Frame(playlist_window)
                song_frame.pack(anchor="w")
                tk.Label(song_frame, text=f"{i + 1}. {os.path.basename(song)}").pack(side="left")
                tk.Button(song_frame, text="Delete", command=lambda idx=i: delete_song(idx)).pack(side="left")
        else:
            tk.Label(playlist_window, text="No songs in playlist").pack()


def main():
    pygame.init()
    root = tk.Tk()
    music_player = MusicPlayer(root)

    show_playlist_button = tk.Button(root, text="Show Playlist", command=music_player.show_playlist)
    show_playlist_button.pack()

    show_exit_button = tk.Button(root, text="Exit", command=root.quit)
    show_exit_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
