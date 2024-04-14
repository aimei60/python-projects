import pygame
import time

pygame.mixer.init()

def music(song):
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


def play_music():
    user = input("Hi, would you like to listen to some music? We have calm, country, jazz, rock or house: ")
    if user == "calm":
        music('dream-memory-alarm-clock-109567.mp3')
    elif user == "country":
        music('armonica-1-74138.mp3')
    elif user == "house":
        music('edm-drums-tropical-house-loops-1-11276.mp3')
    elif user == "jazz":
        music('jazz-loop-rusted-maid-68244.mp3')
    elif user == "rock":
        music('rock-music-6211.mp3')
    else:
        print("Your choice is invalid to play music")
        
if __name__ == "__main__":
    play_music()
