import pygame
from pygame.locals import * 
from constantes import *


class Labyrinthe:

	def __init__(self, file):
		self.file = file
		self.grid = []



	def generer(self):

		structure = [] # création d'une liste vide
		with open (self.file, "r") as file.txt: # Ouverture du fichier N1.txt
			for ligne in n1.txt: # On parcourt chaque ligne
				for sprite in ligne:
					structure.append(sprite) # On ajoute pour chaque élément un sprite
		self.grid = structure
					


	def afficher(self, screen):
		
		mur = pygame.image.load(IMAGE_MUR).convert()
		depart = pygame.image.load(IMAGE_DEPART).convert()
		arrivee = pygame.image.load(IMAGE_ARRIVEE).convert_alpha()
		
		#On parcourt la liste du niveau
		num_ligne = 0
		for ligne in self.file:
			#On parcourt les listes de lignes
			num_sprite = 0
			for sprite in ligne:
				#On calcule la position réelle en pixels
				x = num_sprite * TAILLE_SPRITE
				y = num_ligne * TAILLE_SPRITE
				if sprite == 'm':		   #m = Mur
					screen.blit(mur, (x,y))
				elif sprite == 'd':		   #d = Départ
					screen.blit(depart, (x,y))
				elif sprite == 'a':		   #a = Arrivée
					screen.blit(arrivee, (x,y))
				num_case += 1
			num_ligne += 1



class Perso:

	def __init__(self):
		self.sprite_x = 0
		self.sprite_y = 0
		self.x = 0
		self.y = 0

	def deplacer (self, direction):

		if direction == "right": # Tourne à droite s'il n'y a pas de mur à droite
			if self.file[self.sprite_y][self.sprite_x+1] != 'm':
				self.sprite_x += 1
			
		if direction == "left": # Tourne à gauche s'il n'y a pas de mur à gauche
			if self.file[self.sprite_y][self.sprite_x-1] != 'm':
				self.sprite_x -= 1

		if direction == "up": # Tourne en haut s'il n'y a pas de mur en haut
			if self.file[self.sprite_y-1][self.sprite_x] != 'm':
				self.sprite_y -= 1

		if direction == "down": # Tourne en bas s'il n'y a pas de mur en bas
			if self.file[self.sprite_y+1][self.sprite_x] != 'm':
				self.sprite_y += 1

class Items:

	def __init__ (self):
		self.x = 0
		self.y = 0
		self.sprite_x = 0
		self.sprite_y = 0