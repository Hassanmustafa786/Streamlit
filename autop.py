import pygame
import time

def play_audio(file_path):
    pygame.init()
    pygame.mixer.init()

    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        pygame.event.wait()  # Wait until the music finishes playing
    except pygame.error as e:
        print(f"Error: {e}")

file_path = "translate.mp3"
play_audio(file_path)
time.sleep(10)