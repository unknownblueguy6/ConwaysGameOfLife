import pygame, sys, pickle, platform
# from timeit import default_timer as timer
from pygame.locals import *

CELL_SIZE = 12
CELLS_PER_ROW = 50+1
CELLS_PER_COL = 50+1
WINDOWWIDTH = CELLS_PER_COL*CELL_SIZE
WINDOWHEIGHT = CELLS_PER_ROW*CELL_SIZE + 2*CELL_SIZE

FPS = 60

MAX_CELLS_PER_ROW = 1000 + 1
MAX_CELLS_PER_COL = 1000 + 1
DEAD = False
ALIVE = True

DEAD_COLOUR = WHITE = (255, 255, 255)
ALIVE_COLOUR = BLACK = (0, 0, 0)
GREY = (226, 230, 222)
BLUE = (0, 0, 255)

EDIT = 0
RUN = 1

gameState = EDIT
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


def edit():
	global gameState
	x, y = 0, 0
	while True:
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				if event.key == K_LEFT and x != -CELLS_PER_ROW//2:
					x -= 1
				elif event.key == K_RIGHT and x != CELLS_PER_ROW//2:
					x += 1
				elif event.key == K_DOWN and y != CELLS_PER_COL//2:
					y += 1
				elif event.key == K_UP and y != -CELLS_PER_COL//2: 
					y -= 1
				elif event.key == K_s:
					changeState(x, y)
				elif event.key == K_SPACE or event.key == K_RETURN:
					gameState = RUN
					return
		drawGrid()
		pygame.draw.rect(windowSurface, BLUE, pygame.Rect((x + CELLS_PER_ROW//2)* CELL_SIZE, (y + CELLS_PER_COL//2) * CELL_SIZE, CELL_SIZE, CELL_SIZE), 2)
		pygame.display.update()

def update():
	# start = timer()
	global liveCells
	drawGrid()
	
	liveCellsCopy = pickle.loads(pickle.dumps(liveCells))
	
	checkedCells = set()

	for x, y in liveCells:

		for i in range(x -1, x + 2):
			if i == -1 + -MAX_CELLS_PER_ROW//2 or i == MAX_CELLS_PER_ROW//2 + 1:
				continue	
			
			for j in range(y -1 , y +2):
				if (j == -1 + -MAX_CELLS_PER_COL//2) or (j == MAX_CELLS_PER_COL//2 + 1):
					continue
			
				if (i, j) in checkedCells:
					continue

				alive = 0
			
				for k in range(i-1, i+2):
					if k == -1 + -MAX_CELLS_PER_ROW//2 or k == MAX_CELLS_PER_ROW//2 + 1:
						continue
					
					for l in range(j-1, j+2):
						if (l == -1 + -MAX_CELLS_PER_COL//2) or (l == MAX_CELLS_PER_COL//2 + 1) or (k == i and l == j): 
							continue

						if (k, l) in liveCells:
							alive += 1

				if (i, j) in liveCells:
					if not((alive == 2) or (alive == 3)):
						liveCellsCopy.remove((i, j))
				else:
					if alive == 3:
						liveCellsCopy.add((i, j))
				checkedCells.add((i, j))

	liveCells = pickle.loads(pickle.dumps(liveCellsCopy))

	# end = timer()

	#print(end - start)
def exit():
	pygame.quit()
	sys.exit()

init()

while True:
	if(gameState == EDIT):
		edit()
	elif(gameState == RUN):
		update()
	pygame.display.update()
	mainClock.tick(FPS)
	print(mainClock.get_fps())

exit()