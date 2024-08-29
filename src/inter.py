import tkinter as tk
from PIL import Image, ImageTk
import pygame

# === Constants === #
WIDTH = 400
HEIGHT = 100
BG_COLOR = 'lightblue'
BUTTON_COLOR = 'blue'
FONT_H1 = ("Helvatica", 50, 'bold')
COLOR_H1 = 'white'
FONT_H2 = ("Helvatica", 20, 'bold')
COLOR_H2 = 'white'

# === Interface Configuration === #
class Interface:
    def __init__(self, root):
        self.root = root
        self.root.title('Synthetic Radio')
        self.root.minsize(width=WIDTH, 
                          height=HEIGHT)
        self.root.resizable(False, False)

        self.process = 'disabled'
        self.is_playing = False

        self.initialize_widgets()
        self.initialize_player()

    def initialize_widgets(self):
        
        # Initialize the background image
        self.frame_bg = tk.Frame(self.root, 
                                 width=WIDTH, 
                                 height=HEIGHT,
                                 bg=BG_COLOR)
        self.frame_bg.pack()

        self.start_button = tk.Button(self.frame_bg,
                                      width=20,
                                      height=2,
                                      text='START',
                                      command=self.start_process,)
        self.start_button.pack(padx=25, 
                               pady=30, 
                               side='left')

        self.stop_button = tk.Button(self.frame_bg,
                                      width=20,
                                      height=2,
                                      text='STOP',
                                      command=self.stop_process,)
        self.stop_button.pack(padx=25, 
                              pady=30, 
                              side='left')

    def initialize_player(self):
        pygame.init()
        pygame.mixer.init()

    def start_process(self):
        self.process = 'started'

    def stop_process(self):
        self.process = 'stopped'

    def play(self, songfile):
        if not self.is_playing:
            self.current_song = songfile
            pygame.mixer.music.load(self.current_song)
            pygame.mixer.music.play()
            self.is_playing = True

    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False

    def is_finished_playing(self):
        if pygame.mixer.music.get_busy():
            return False
        else:
            return True


if __name__ == '__main__':
    root = tk.Tk()
    interface = Interface(root)
    mainloop = True
    while mainloop:
        root.update()
        response = interface.process
        
        # Force close application
        try:
            root.state()
        except tk.TclError as e:
            break


