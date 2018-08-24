import pygame, sys, copy, platform
from pygame.locals import *

CELL_SIZE = 9
CELLS_PER_ROW = 50+1
CELLS_PER_COL = 50+1
WINDOWWIDTH = CELLS_PER_COL*CELL_SIZE
WINDOWHEIGHT = CELLS_PER_ROW*CELL_SIZE + 2*CELL_SIZE


MAX_CELLS_PER_ROW = 100 + 1
MAX_CELLS_PER_COL = 100 + 1
DEAD = False
ALIVE = True

DEAD_COLOUR = WHITE = (255, 255, 255)
ALIVE_COLOUR = BLACK = (0, 0, 0)
GREY = (226, 230, 222)

class Cell:
	size = CELL_SIZE

	def __init__(self, x, y):
		self.x = x 
		self.y = y
		self.state = DEAD
		self.colour = DEAD_COLOUR

	def activate(self):
		self.state = ALIVE
		self.colour = ALIVE_COLOUR

	def deactivate(self):
		self.state = DEAD
		self.colour = DEAD_COLOUR

	def draw(self):
		pygame.draw.rect(windowSurface, self.colour, pygame.Rect((self.x+int(CELLS_PER_ROW/2))* self.size, (self.y+int(CELLS_PER_COL/2)) * self.size, self.size, self.size))
		pygame.draw.rect(windowSurface, GREY, pygame.Rect((self.x+int(CELLS_PER_ROW/2))* self.size, (self.y+int(CELLS_PER_COL/2)) * self.size, self.size, self.size), 1)

grid = []

def init():
	pygame.init()
	global windowSurface
	global mainClock
	mainClock = pygame.time.Clock()
	windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
	windowSurface.fill(WHITE)
	pygame.display.set_caption("Conway's Game of Life")

	for i in range(MAX_CELLS_PER_ROW):
		grid.append([])
		for j in range(MAX_CELLS_PER_COL):
			grid[i].append(Cell(i-int(MAX_CELLS_PER_ROW/2), j-int(MAX_CELLS_PER_COL/2)))


def getCell(x, y):
	global grid
	return grid[x+int(MAX_CELLS_PER_ROW/2)][y+int(MAX_CELLS_PER_COL/2)]

def getX():
	global grid
	x1 = MAX_CELLS_PER_ROW
	x2 = -MAX_CELLS_PER_ROW
	for row in grid:
		for cell in row:
			if cell.state == ALIVE :
				if cell.x < x1:
					x1 = cell.x
				if cell.x > x2:
					x2 = cell.x
	return x1 - 1, x2 + 2

def getY():
	global grid
	y1 = MAX_CELLS_PER_COL
	y2 = -MAX_CELLS_PER_COL
	for row in grid:
		for cell in row:
			if cell.state == ALIVE :
				if cell.y < y1:
					y1 = cell.y
				if cell.y > y2:
					y2 = cell.y
	return y1 - 1, y2 + 2

def update():
	global grid
	
	for i in range(-int(CELLS_PER_ROW/2), int(CELLS_PER_ROW/2) + 1):
		for j in range(-int(CELLS_PER_COL/2), int(CELLS_PER_COL/2) + 1):
			getCell(i, j).draw()
	
	gridCopy = copy.deepcopy(grid)

	x1, x2 = getX()
	y1, y2 = getY()

	print("%s %s" % (x1, x2))
	print("%s %s" % (y1, y2))
	
	for i in range(x1, x2):
		for j in range(y1, y2):

			alive = 0
			
			for k in range(i-1, i+2):
				if k == -1 or k == len(grid):
					continue
					
				for l in range(j-1, j+2):
					if (l == -1 + -int(MAX_CELLS_PER_COL/2)) or (l == int(MAX_CELLS_PER_COL/2) + 1) or (k == i and l == j): 
						continue

					if getCell(k, l).state == ALIVE:
						alive += 1

			if getCell(i, j).state == ALIVE:
				if not((alive == 2) or (alive == 3)):
					gridCopy[i + int(MAX_CELLS_PER_ROW/2)][j + int(MAX_CELLS_PER_COL/2)].deactivate()
			else:
				if alive == 3:
					gridCopy[i + int(MAX_CELLS_PER_ROW/2)][j + int(MAX_CELLS_PER_COL/2)].activate()

	grid = copy.deepcopy(gridCopy)

def exit():
	pygame.quit()
	sys.exit()

init()

#glider, just for testing
# grid[10][8].activate()
# grid[11][9].activate()
getCell(0,0).activate()
getCell(1,1).activate()
getCell(2,0).activate()
getCell(2,1).activate()
getCell(1,2).activate()	

# getCell(0, 0).activate()

# for i in range(-int(CELLS_PER_ROW/2), int(CELLS_PER_ROW/2) + 1):
# 	for j in range(-int(CELLS_PER_COL/2), int(CELLS_PER_COL/2) + 1):
# 		getCell(i, j).draw()
# pygame.display.update()

while True:
	update()
	pygame.display.update()
	mainClock.tick(1000)

exit()