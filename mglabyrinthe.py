#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Jeu Mac Gyver Labyrinthe
Jeu dans lequel on doit déplacer MG jusqu'aux items à travers un labyrinthe pour les ramener au gardien.

Script Python
Fichiers : mglabyrinthe.py, classes.py, constantes.py, n1 + images
"""

import pygame
from pygame.locals import *

from classes import *
from constantes import *

# On initialise pygame, permettant de charger tous les modules de pygame et les initialiser.
pygame.init() 

#  Ouverture de la fenêtre Pygame (carré : largeur = hauteur)
screen = pygame.display.set_mode((COTE_FENETRE,COTE_FENETRE))
pygame.display.set_caption("Aidez Mac Gyver !")

# Image de fond du jeu
background = pygame.image.load(IMAGE_FOND).convert()
screen.blit(background, (0,0)) 

mg = pygame.image.load(IMAGE_MACGYVER).convert_alpha()
pygame.display.set_icon(mg)
position_mg = mg.get_rect()
screen.blit(mg, (position_mg))



continuer = 1
while continuer:


	pygame.key.set_repeat(400, 30)
	pygame.time.Clock().tick(30)

	for event in pygame.event.get():	#Attente des événements
		
		if event.type == QUIT: #Si "quitte"
			continuer = 0

		if event.type == KEYDOWN:
			if event.key == K_DOWN:	#Si "flèche bas"
				#On descend le perso
				mg.deplacer('down')

		if event.type == KEYDOWN:
			if event.key == K_UP:	#Si "flèche haut"
				mg.deplacer('up')

		if event.type == KEYDOWN:
			if event.key == K_RIGHT:	#Si "flèche droite"
				mg.deplacer('right')

		if event.type == KEYDOWN:
			if event.key == K_LEFT:	#Si "flèche gauche"
				mg.deplacer('left')

		


	#Re-collage
	screen.blit(background, (0,0))	
	screen.blit(mg, position_mg)
	#Rafraichissement
	pygame.display.flip()