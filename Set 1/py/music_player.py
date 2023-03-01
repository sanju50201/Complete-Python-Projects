import pygame
import tkinter as tk
from tkinter import filedialog

# Initialize the pygame
pygame.init()

# create the UI

root = tk.Tk()
root.title("Music Player")
root.geometry("300x300")


# function to handle file selection
def select_file():
    file_path = filedialog.askopenfilename()
    pygame.mixer.music.load(file_path)


# function to handle play button
def play_music():
    pygame.mixer.music.play()

# function to handle pause button


def pause_music():
    pygame.mixer.music.pause()

# function to handle resume button


def resume_music():
    pygame.mixer.music.unpause()

# function to handle stop button


def stop_music():
    pygame.mixer.music.stop()


# create the buttons
file_button = tk.Button(root, text="Select File ", command=select_file)
file_button.pack()

play_button = tk.Button(root, text="Play", command=play_music)
play_button.pack()

pause_button = tk.Button(root, text="Pause", command=pause_music)
pause_button.pack()

resume_button = tk.Button(root, text="Resume", command=resume_music)
resume_button.pack()

stop_button = tk.Button(root, text="Stop", command=stop_music)
stop_button.pack()

# run the UI loop
root.mainloop()

# clean up pygame
pygame.quit()
