#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""

Labyrinth classes

"""
import random

from constantes import (FILE, NB_SPRITE, SPRITE_SIZE, WINDOW, WALL, DEPARTURE, ARRIVAL, GUARDIAN, MG)


class Labyrinth:
	"""
	This class object 'Labyrinth' allow to define the maze.
	We have .......
	"""

	def __init__(self):
		self.file = FILE
		self.grid = []
		self.generate()
		self.x_value = 0
		self.y_value = 0

	def generate(self):
		"""
		Method which create the structure from the file map/N1.txt.
		"""
		structure = []
		# Create a list of lists.
		with open(self.file, "r") as file:
			for ligne in file:
				to_add = []
				for character in ligne:
					if character != '\n':
						to_add.append(character)
				structure.append(to_add)
		self.grid = structure

	def display(self):
		"""
		Method wich that allows to put a visual form for our labyrinth:
		to 'm' an image of a wall;
		to 'd' an image of a departure;
		to 'a' an image of a arrival;
		and to 'g' an image of a guardian.
		For each sprites in ligne we attribute coordinates (x,y)
		"""
		# We start the first list to the first line.
		num_ligne = 0
		for ligne in self.grid:
			num_sprite = 0
			for sprite in ligne:
				self.x_value = num_sprite * SPRITE_SIZE
				self.y_value = num_ligne * SPRITE_SIZE
				if sprite == 'm':		   # m = "Mur".
					WINDOW.blit(WALL, (self.x_value, self.y_value))
				elif sprite == 'd':		   # d = "Départ".
					WINDOW.blit(DEPARTURE, (self.x_value, self.y_value))
				elif sprite == 'a':		   # a = "Arrivée".
					WINDOW.blit(ARRIVAL, (self.x_value, self.y_value))
				elif sprite == 'g':
					WINDOW.blit(DEPARTURE, (self.x_value, self.y_value))
					WINDOW.blit(GUARDIAN, (self.x_value, self.y_value))
				num_sprite += 1
			num_ligne += 1


class Heroe:
	"""
	Class wich define a character, with his position (x,y), his picture.
	This one can move inside the labyrinth except in wall and out of screen.
	"""

	def __init__(self):
		self.pos_x = 0
		self.pos_y = 0
		self.x_value = 0
		self.y_value = 0
		self.sprite = MG

	def move(self, direction, grid):
		"""
		Method wich define the character's abilities to move in the labyrinth.
		"""
		# Move to the right.
		if direction == "right":
			if self.pos_x < (NB_SPRITE - 1): # To avoid going out of screen.
				if grid[self.pos_y][self.pos_x+1] != 'm' and grid[self.pos_y][self.pos_x+1] != 'g':
				# To avoid going out of wall or guardian
					self.pos_x += 1
					self.x_value = self.pos_x * SPRITE_SIZE

		# Move to the left.
		if direction == "left":
			if self.pos_x > 0: # To avoid going out of screen.
				if grid[self.pos_y][self.pos_x-1] != 'm':
				# To avoid going out of wall.
					self.pos_x -= 1
					self.x_value = self.pos_x * SPRITE_SIZE

		# Move to the top.
		if direction == "top":
			if self.pos_y > 0: # To avoid going out of screen.
				if grid[self.pos_y-1][self.pos_x] != 'm':
				# to avoid going out of wall.
					self.pos_y -= 1
					self.y_value = self.pos_y * SPRITE_SIZE

		# Move to the bottom.
		if direction == "bottom":
			if self.pos_y < (NB_SPRITE - 1): # To avoid going out of screen.
				if grid[self.pos_y+1][self.pos_x] != 'm':
				# To avoid going out of wall.
					self.pos_y += 1
					self.y_value = self.pos_y * SPRITE_SIZE


class Items:
	"""
	Class which define 3 items (ether, tube and syringue) with coordinates, images.
	These items must have random coordinates.
	These items must be farmed by the main character.
	"""

	coordinates_elements = []

	def __init__(self, picture, name):
		self.pos_x = 0
		self.pos_y = 0
		self.x_value = 0
		self.y_value = 0
		self.sprite = picture
		self.name = name
		self.collected = False

	def locate_items(self, grid):
		"""
		Method which define random coordinates for each items.
		For that we create a dictionnary with all possible coordinates (accessible by the main character).
		The, we use the function 'randomn' in this list to select coordinates (column,ligne).
		"""
		coordinates = ()
		position = []

		num_ligne = 0
		while num_ligne < NB_SPRITE:
			num_column = 1 # We remove the first cell - cell[0] = departure.
			while num_column < NB_SPRITE:
				if grid[num_ligne][num_column] == '0': # We select only coordinates in empty cells.
					coordinates = (num_column, num_ligne)
					position.append(coordinates)
				num_column += 1
			num_ligne += 1

		tmp = random.sample(position, 1)
		if tmp not in Items.coordinates_elements: # To avoid duplicates coordinates.
			Items.coordinates_elements.append(tmp)

		self.pos_x, self.pos_y = tmp[0]
		self.x_value = self.pos_x * SPRITE_SIZE
		self.y_value = self.pos_y * SPRITE_SIZE

	def farming(self, mgpos):
		"""
		Method which define if items are collected by the main character, only if coordinates are equal.
		"""
		if mgpos.pos_x == self.pos_x and mgpos.pos_y == self.pos_y:
			self.collected = True
			
