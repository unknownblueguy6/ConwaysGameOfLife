import pygame, sys, platform
from pygame.locals import *

CELL_SIZE = 10
CELLS_PER_ROW = 50
CELLS_PER_COL = 50
WINDOWWIDTH = CELLS_PER_COL*SIZE
WINDOWHEIGHT = CELLS_PER_ROW*SIZE + 2*SIZE

DEAD = False
ALIVE = True

DEAD_COLOUR = WHITE = (255, 255, 255)
ALIVE_COLOUR = BLACK = (0, 0, 0)

class Cell
	size = CELL_SIZE

	def _init_(self, x, y):
		self.x = x
		self.y = y
		self.rect = pygame.Rect(x, y, size, size)
		self.state = DEAD
		self.colour = DEAD_COLOUR

	def activate(self):
		self.state = ALIVE
		self.colour = ALIVE_COLOUR

	def blit(self):
		pygame.draw.rect(windowSurface, self.colour, self.rect)

grid = []

#Immediate fixes required here
for i in range CELLS_PER_ROW:
	grid.append([])
	for j in range CELLS_PER_COL:
		grid[i].append(Cell())

def exit():
	pygame.quit()
	sys.exit()