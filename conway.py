import pygame, sys, copy, platform
from pygame.locals import *

CELL_SIZE = 10
CELLS_PER_ROW = 50
CELLS_PER_COL = 50
WINDOWWIDTH = CELLS_PER_COL*CELL_SIZE
WINDOWHEIGHT = CELLS_PER_ROW*CELL_SIZE + 2*CELL_SIZE

DEAD = False
ALIVE = True

DEAD_COLOUR = WHITE = (255, 255, 255)
ALIVE_COLOUR = BLACK = (0, 0, 0)
GREY = (226, 230, 222)

class Cell:
	size = CELL_SIZE

	def __init__(self, x, y):
		self.x = x * self.size
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
		pygame.draw.rect(windowSurface, GREY, self.rect, 1)

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


def convertCoord(x, y):
	return (CELLS_PER_ROW/2, CELLS_PER_COL/2 - y)


def update():
	global grid
	for row in grid:
		for cell in row:
			cell.draw()
	gridCopy = copy.deepcopy(grid)

	for i in range(len(grid)):
		for j in range(len(grid[i])):

			alive = 0
			
			for k in range(i-1, i+2):
				if k == -1 or k == len(grid):
					continue
					
				for l in range(j-1, j+2):
					if (l == -1) or (l == len(grid[i])) or (k == i and l == j): 
						continue

					if grid[k][l].state == ALIVE:
						alive += 1

			if grid[i][j].state == ALIVE:
				if not((alive == 2) or (alive == 3)):
					gridCopy[i][j].deactivate()
			else:
				if alive == 3:
					gridCopy[i][j].activate()

	grid = copy.deepcopy(gridCopy)

def exit():
	pygame.quit()
	sys.exit()

init()

#glider, just for testing
grid[10][8].activate()
grid[11][9].activate()
grid[10][10].activate()
grid[11][11].activate()
grid[12][10].activate()
grid[12][11].activate()
grid[11][12].activate()	


while True:
	update()
	pygame.display.update()
	mainClock.tick(10)

exit()