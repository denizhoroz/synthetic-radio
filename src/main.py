import tkinter as tk
from inter import Interface
import os
import random

SONGS_FILE = 'songdb'

def load_songs(songs_folder):
    song_list = os.listdir(songs_folder)
    return song_list

def select_song(song_list):
    selected_song = random.choice(song_list)
    return selected_song


if __name__ == '__main__':
    song_list = load_songs(SONGS_FILE)

    # Start the interface
    root = tk.Tk()
    interface = Interface(root)
    mainloop = True
    while mainloop:
        root.update()
        process = interface.process

        selected_song = select_song(song_list)
        
        if process == 'started':
            interface.play(f'{SONGS_FILE}/{selected_song}')
        elif process == 'stopped':
            interface.stop()
            
        # Force close application
        try:
            root.state()
        except tk.TclError as e:
            break
