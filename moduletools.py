import pygame
import time
import random
from pathlib import Path

def listAllFiles(dir):
    dir_path = dir  

    files = [item.name for item in dir_path.iterdir() if item.is_file()]
    if ".DS_Store" in files:
        files.remove(".DS_Store")
    return files


class RandomSongPicker:
    "A class to randomly pick a song file"
    def __init__(self):
        self.mydir = f"{Path.cwd()}/Music"
        self.list_of_files = listAllFiles(Path(f"{Path.cwd()}/Music"))
    def pick(self):
        pickedchoice = random.choice(self.list_of_files)
        return pickedchoice


t = RandomSongPicker()
i = t.pick()
l = f"Music/{i}"
print(l)



# TEST: PYGAME TIME
pygame.mixer.init()
pygame.mixer.music.load(l)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    time.sleep(1)