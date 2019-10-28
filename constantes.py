#!/usr/bin/python3
# -*-coding:utf-8 -

"""
Labyrinth constants
"""

import pygame

pygame.init()

# Dimensions of labyrinth
NB_SPRITE = 15
SPRITE_SIZE = 30
SCREEN_SIDE = NB_SPRITE * SPRITE_SIZE

# Customization window...
WINDOW = pygame.display.set_mode((SCREEN_SIDE + 90, SCREEN_SIDE))
# Without this line, 'ICON' will be a misstake.
# + 60 px for items scoreboard.
WINDOW_TITLE = "Help Mac Gyver to escape !"
ICON = pygame.image.load("images/macgyver.png").convert_alpha()

# Customization window home
WINDOW_HOME = pygame.Surface((540, 450))
FONT = pygame.font.Font('freesansbold.ttf', 40)
SENTENCE1 = "- Mac Gyver Game -"
SENTENCE2 = "Play  :  press 'SPACE'"
SENTENCE3 = "QUIT  :  press 'ESCAPE'"

HOME_WINDOW_TITLE1 = FONT.render(SENTENCE1, True, (255, 255, 255))
HOME_WINDOW_TITLE_RECT1 = HOME_WINDOW_TITLE1.get_rect()
HOME_WINDOW_TITLE_RECT1.center = (270, 50)

HOME_WINDOW_TITLE2 = FONT.render(SENTENCE2, False, (255, 200, 200))
HOME_WINDOW_TITLE_RECT2 = HOME_WINDOW_TITLE2.get_rect()
HOME_WINDOW_TITLE_RECT2.center = (270, 200)

HOME_WINDOW_TITLE3 = FONT.render(SENTENCE3, False, (255, 200, 200))
HOME_WINDOW_TITLE_RECT3 = HOME_WINDOW_TITLE3.get_rect()
HOME_WINDOW_TITLE_RECT3.center = (270, 300)

# Customization items window
FONT = pygame.font.Font('freesansbold.ttf', 10)
ITEMS_WINDOW_TITLE = FONT.render("Items collected:", True, (255, 255, 255))

SURFACE_ETHER = pygame.Surface((30, 30))
SURFACE_ETHER.fill((255, 255, 255))
SURFACE_TUBE = pygame.Surface((30, 30))
SURFACE_TUBE.fill((255, 255, 255))
SURFACE_SYRINGUE = pygame.Surface((30, 30))
SURFACE_SYRINGUE.fill((255, 255, 255))

# Labyrinth elements
BACKGROUND = pygame.image.load("images/fond.jpg").convert()
WALL = pygame.image.load("images/mur.jpg").convert()
WALL = pygame.transform.scale(WALL, (SPRITE_SIZE, SPRITE_SIZE))
DEPARTURE = pygame.image.load("images/depart.jpg").convert()
DEPARTURE = pygame.transform.scale(DEPARTURE, (SPRITE_SIZE, SPRITE_SIZE))
ARRIVAL = pygame.image.load("images/arrivee.jpg").convert()
ARRIVAL = pygame.transform.scale(ARRIVAL, (SPRITE_SIZE, SPRITE_SIZE))

# Labyrinth items
TUBE = pygame.image.load("images/tube_plastique.png").convert_alpha()
TUBE = pygame.transform.scale(TUBE, (SPRITE_SIZE, SPRITE_SIZE))
ETHER = pygame.image.load("images/ether.png").convert_alpha()
ETHER = pygame.transform.scale(ETHER, (SPRITE_SIZE, SPRITE_SIZE))
SYRINGUE = pygame.image.load("images/seringue.png").convert_alpha()
SYRINGUE = pygame.transform.scale(SYRINGUE, (SPRITE_SIZE, SPRITE_SIZE))

# Display characters
MG = pygame.image.load("images/MacGyver.png").convert_alpha()
MG = pygame.transform.scale(MG, (SPRITE_SIZE, SPRITE_SIZE))
GUARDIAN = pygame.image.load("images/Gardien.png").convert_alpha()
GUARDIAN = pygame.transform.scale(GUARDIAN, (SPRITE_SIZE, SPRITE_SIZE))

# Win & Lose
WIN = pygame.image.load("images/win.jpg").convert()
WIN = pygame.transform.scale(WIN, (SCREEN_SIDE + 90, SCREEN_SIDE))
GAMEOVER = pygame.image.load("images/gameover.png").convert()
GAMEOVER = pygame.transform.scale(GAMEOVER, (SCREEN_SIDE + 90, SCREEN_SIDE))

# Structure labyrinthe
FILE = "map/N1.txt"

# Sounds
SOUNDTRACK = pygame.mixer.Sound('sounds/sound_game.wav')
SOUNDTRACK.set_volume(.1)
