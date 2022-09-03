import pygame

import random


# plays button sound
def button_sound():
    press = pygame.mixer.Sound('Sounds/button_press.wav')
    pygame.mixer.Sound.play(press)


# plays a random song for the main menu
def start_menu_music():
    random_song = random.randrange(3)
    pygame.mixer.music.load('Sounds/{}'.format(menu_music[random_song]))
    pygame.mixer.music.play(-1)


# plays a random song for playing a game
def start_playing_music():
    random_song = random.randrange(7)
    pygame.mixer.music.load('Sounds/{}'.format(game_music[random_song]))
    pygame.mixer.music.play(-1)


# lists of the names of the music files
menu_music = ['menu_music1.wav', 'menu_music2.wav', 'menu_music3.wav']
game_music = ['music1.wav', 'music2.wav', 'music3.wav', 'music4.wav', 'music5.wav', 'music6.wav', 'music7.wav']

