import pygame, sys, copy, platform
from timeit import default_timer as timer
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

grid = []

def init():
	pygame.init()
	global windowSurface
	global mainClock
	mainClock = pygame.time.Clock()
	windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), DOUBLEBUF)
	windowSurface.fill(WHITE)
	pygame.display.set_caption("Conway's Game of Life")

	for i in range(MAX_CELLS_PER_ROW):
		grid.append([])
		for j in range(MAX_CELLS_PER_COL):
			grid[i].append(False)


def getCell(x, y):
	global grid
	return grid[x+int(MAX_CELLS_PER_ROW/2)][y+int(MAX_CELLS_PER_COL/2)]

def changeState(x, y):
	global grid
	grid[x+int(MAX_CELLS_PER_ROW/2)][y+int(MAX_CELLS_PER_COL/2)] = not(grid[x+int(MAX_CELLS_PER_ROW/2)][y+int(MAX_CELLS_PER_COL/2)])

def drawCell(x, y):
	if(getCell(x,y) == ALIVE):
		colour = ALIVE_COLOUR
	else:
		colour = DEAD_COLOUR
	pygame.draw.rect(windowSurface, colour, pygame.Rect((x+int(CELLS_PER_ROW/2))* CELL_SIZE, (y+int(CELLS_PER_COL/2)) * CELL_SIZE, CELL_SIZE, CELL_SIZE))
	pygame.draw.rect(windowSurface, GREY, pygame.Rect((x+int(CELLS_PER_ROW/2))* CELL_SIZE, (y+int(CELLS_PER_COL/2)) * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

def getX():
	global grid
	x1 = MAX_CELLS_PER_ROW
	x2 = -MAX_CELLS_PER_ROW
	for i in range(-int(MAX_CELLS_PER_ROW/2), int(MAX_CELLS_PER_ROW/2) + 1):
		for j in range(-int(MAX_CELLS_PER_COL/2), int(MAX_CELLS_PER_COL/2) + 1):
			if getCell(i, j) == ALIVE :
				if i < x1:
					x1 = i
				if i > x2:
					x2 = i
	return x1 - 1, x2 + 2

def getY():
	global grid
	y1 = MAX_CELLS_PER_COL
	y2 = -MAX_CELLS_PER_COL
	for i in range(-int(MAX_CELLS_PER_ROW/2), int(MAX_CELLS_PER_ROW/2) + 1):
		for j in range(-int(MAX_CELLS_PER_COL/2), int(MAX_CELLS_PER_COL/2) + 1):
			if getCell(i, j) == ALIVE :
				if j < y1:
					y1 = j
				if j > y2:
					y2 = j
	return y1 - 1, y2 + 2

def update():
	
	global grid
	
	for i in range(-int(CELLS_PER_ROW/2), int(CELLS_PER_ROW/2) + 1):
		for j in range(-int(CELLS_PER_COL/2), int(CELLS_PER_COL/2) + 1):
			drawCell(i, j)
	
	gridCopy = copy.deepcopy(grid)

	start = timer()
	x1, x2 = getX()
	y1, y2 = getY()
	end = timer()

	print(end - start)
	
	#print("%s,%s %s,%s" % (x1,y1, x2,y2))
	
	for i in range(x1, x2):
		for j in range(y1, y2):

			alive = 0
			
			for k in range(i-1, i+2):
				if k == -1 or k == len(grid):
					continue
					
				for l in range(j-1, j+2):
					if (l == -1 + -int(MAX_CELLS_PER_COL/2)) or (l == int(MAX_CELLS_PER_COL/2) + 1) or (k == i and l == j): 
						continue

					if getCell(k, l) == ALIVE:
						alive += 1

			if getCell(i, j) == ALIVE:
				if not((alive == 2) or (alive == 3)):
					gridCopy[i + int(MAX_CELLS_PER_ROW/2)][j + int(MAX_CELLS_PER_COL/2)] = False
			else:
				if alive == 3:
					gridCopy[i + int(MAX_CELLS_PER_ROW/2)][j + int(MAX_CELLS_PER_COL/2)] = True

	grid = copy.deepcopy(gridCopy)

def exit():
	pygame.quit()
	sys.exit()

init()

#glider, just for testing
# grid[10][8] = True
# grid[11][9] = True
changeState(0,0)
changeState(1,1)
changeState(2,0)
changeState(2,1)
changeState(1,2)

# getCell(0, 0) = True

# for i in range(-int(CELLS_PER_ROW/2), int(CELLS_PER_ROW/2) + 1):
# 	for j in range(-int(CELLS_PER_COL/2), int(CELLS_PER_COL/2) + 1):
# 		getCell(i, j).draw()
# pygame.display.update()

while True:
	update()
	pygame.display.update()
	mainClock.tick(1000)

exit()