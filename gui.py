import pygame, sys
from pygame.locals import *

CELL_SIZE = 12
CELLS_PER_ROW = 50+1
CELLS_PER_COL = 50+1
WINDOWWIDTH = CELLS_PER_COL*CELL_SIZE
WINDOWHEIGHT = CELLS_PER_ROW*CELL_SIZE +  2*CELL_SIZE

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (226, 230, 222)
BLUE = (0, 0, 255)

DEAD_COLOUR = WHITE
ALIVE_COLOUR = BLACK

liveCells = set()

def init():
	pygame.init()
	global windowSurface
	global mainClock
	mainClock = pygame.time.Clock()
	windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), DOUBLEBUF)
	windowSurface.fill(WHITE)
	pygame.display.set_caption("Conway's Game of Life")

def changeState(x, y):
	global liveCells
	if (x, y) in liveCells: 
		liveCells.remove((x, y))
	else:
		liveCells.add((x, y))

def drawCell(x, y):
	if (x, y)  in liveCells:
		colour = ALIVE_COLOUR
	else:
		colour = DEAD_COLOUR
	pygame.draw.rect(windowSurface, colour, pygame.Rect((x + CELLS_PER_ROW//2)* CELL_SIZE, (y + CELLS_PER_COL//2) * CELL_SIZE, CELL_SIZE, CELL_SIZE))
	pygame.draw.rect(windowSurface, GREY, pygame.Rect((x + CELLS_PER_ROW//2)* CELL_SIZE, (y + CELLS_PER_COL//2) * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)


def drawGrid():
	for i in range(-CELLS_PER_ROW//2, CELLS_PER_ROW//2 + 1):
		for j in range(-CELLS_PER_COL//2, CELLS_PER_COL//2 + 1):
			drawCell(i, j)
	pygame.draw.line(windowSurface, GREY, (0, CELLS_PER_COL * CELL_SIZE), (WINDOWWIDTH, CELLS_PER_COL * CELL_SIZE), 1)

def exit():
	pygame.quit()
	sys.exit()