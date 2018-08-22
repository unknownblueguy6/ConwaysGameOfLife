import pygame, sys, platform
from pygame.locals import *

CELL_SIZE = 10
CELLS_PER_ROW = 60
CELLS_PER_COL = 60
WINDOWWIDTH = CELLS_PER_COL*CELL_SIZE
WINDOWHEIGHT = CELLS_PER_ROW*CELL_SIZE + 2*CELL_SIZE

DEAD = False
ALIVE = True

DEAD_COLOUR = WHITE = (255, 255, 255)
ALIVE_COLOUR = BLACK = (0, 0, 0)

class Cell:
	size = CELL_SIZE

	def __init__(self, x, y):
		self.x = x * self.size;
		self.y = y * self.size
		self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
		self.state = DEAD
		self.colour = DEAD_COLOUR

	def activate(self):
		self.state = ALIVE
		self.colour = ALIVE_COLOUR

	def deactivate(self):
		self.state = DEAD
		self.colour = DEAD_COLOUR

	def draw(self):
		pygame.draw.rect(windowSurface, self.colour, self.rect)

grid = []

def init():
	pygame.init()
	global windowSurface
	global mainClock
	mainClock = pygame.time.Clock()
	windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
	windowSurface.fill(WHITE)
	pygame.display.set_caption("Conway's Game of Life")

	for i in range(CELLS_PER_ROW):
		grid.append([])
		for j in range(CELLS_PER_COL):
			grid[i].append(Cell(i, j))

def update():
	for i in range(1, len(grid)-1):
		for j in range(1, len(grid[i])-1):
			if (grid[i][j].state == ALIVE):
				alive = 0
				for k in range(i-1, i+2):
					for l in range(j-1, j+2):
						if k == l : 
							continue
						if grid[j][k].state == ALIVE:
							alive += 1
				if (alive != 2) or (alive != 3):
					grid[i][j].deactivate()
			else:
				alive = 0
				for k in range(i-1, i + 2):
					for l in range(j-1, j+2):
						if k == l : 
							continue
						if grid[j][k].state == ALIVE:
							alive += 1
				if alive == 3:
					grid[i][j].activate()
			grid[i][j].draw()

def exit():
	pygame.quit()
	sys.exit()

init()

grid[30][30].activate()
grid[30][32].activate()
grid[31][32].activate()
grid[31][31].activate()
grid[32][31].activate()

while True:
	update()
	pygame.display.update()
	mainClock.tick(1)

exit()