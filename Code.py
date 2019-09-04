
import pygame
from pygame.locals import *

pygame.init() # On initialise pygame, permettant de charger tous les modules de pygame et les initialiser.

screen = pygame.display.set_mode((1200,1200))
pygame.display.set_caption("Aidez Mac Gyver !")

background = pygame.image.load("background.jpg").convert()
screen.blit(background, (0,0)) 

macgyver = pygame.image.load("MacGyver.png").convert_alpha()
pygame.display.set_icon(macgyver)
position_mac_gyver = macgyver.get_rect()
screen.blit(macgyver, position_mac_gyver)

pygame.display.flip()

pygame.key.set_repeat(400, 30)

continuer = 1
while continuer:
	for event in pygame.event.get():	#Attente des événements
		if event.type == QUIT:
			continuer = 0
		if event.type == KEYDOWN:
			if event.key == K_DOWN:	#Si "flèche bas"
				#On descend le perso
				position_mac_gyver = position_mac_gyver.move(0,3)
		if event.type == KEYDOWN:
			if event.key == K_UP:	#Si "flèche haut"
				position_mac_gyver = position_mac_gyver.move(0,-3)
		if event.type == KEYDOWN:
			if event.key == K_RIGHT:	#Si "flèche droite"
				position_mac_gyver = position_mac_gyver.move(3,0)
		if event.type == KEYDOWN:
			if event.key == K_LEFT:	#Si "flèche gauche"
				position_mac_gyver = position_mac_gyver.move(-3,0)
		


	#Re-collage
	screen.blit(background, (0,0))	
	screen.blit(macgyver, position_mac_gyver)
	#Rafraichissement
	pygame.display.flip()