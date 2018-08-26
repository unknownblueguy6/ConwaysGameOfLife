import pygame, sys, pickle, platform
# from timeit import default_timer as timer
from pygame.locals import *

CELL_SIZE = 10
CELLS_PER_ROW = 50+1
CELLS_PER_COL = 50+1
WINDOWWIDTH = CELLS_PER_COL*CELL_SIZE
WINDOWHEIGHT = CELLS_PER_ROW*CELL_SIZE + 2*CELL_SIZE


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
grid = []
liveCells = set()

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
			grid[i].append(DEAD)


def getCell(x, y):
	global grid
	return grid[x + MAX_CELLS_PER_ROW//2][y + MAX_CELLS_PER_COL//2]

def changeState(x, y):
	global grid
	global liveCells
	state = grid[x + MAX_CELLS_PER_ROW//2][y + MAX_CELLS_PER_COL//2]
	if state == ALIVE : 
		grid[x + MAX_CELLS_PER_ROW//2][y + MAX_CELLS_PER_COL//2] = not state
		liveCells.remove((x, y))
	else:
		grid[x + MAX_CELLS_PER_ROW//2][y + MAX_CELLS_PER_COL//2] = not state
		liveCells.add((x, y))

def drawCell(x, y):
	if(getCell(x,y) == ALIVE):
		colour = ALIVE_COLOUR
	else:
		colour = DEAD_COLOUR
	pygame.draw.rect(windowSurface, colour, pygame.Rect((x + CELLS_PER_ROW//2)* CELL_SIZE, (y + CELLS_PER_COL//2) * CELL_SIZE, CELL_SIZE, CELL_SIZE))
	pygame.draw.rect(windowSurface, GREY, pygame.Rect((x + CELLS_PER_ROW//2)* CELL_SIZE, (y + CELLS_PER_COL//2) * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

def getCoords():
	global liveCells
	x1 =  MAX_CELLS_PER_ROW
	x2 = -MAX_CELLS_PER_ROW
	y1 =  MAX_CELLS_PER_COL
	y2 = -MAX_CELLS_PER_COL
	for x,y in liveCells:
		if x < x1:
			x1 = x
		if x > x2:
			x2 = x
		if y < y1:
			y1 = y
		if y > y2:
			y2 = y
	return x1- 1, x2 + 2, y1 - 1, y2 + 2


def drawGrid():
	global grid
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
	global grid
	global liveCells
	drawGrid()
	
	gridCopy = pickle.loads(pickle.dumps(grid))
	liveCellsCopy = pickle.loads(pickle.dumps(liveCells))

	
	x1, x2, y1, y2 = getCoords()
	

	for i in range(x1, x2):
		for j in range(y1, y2):

			alive = 0
			
			for k in range(i-1, i+2):
				if k == -1 + -MAX_CELLS_PER_ROW//2 or k == MAX_CELLS_PER_ROW//2 + 1:
					continue
					
				for l in range(j-1, j+2):
					if (l == -1 + -MAX_CELLS_PER_COL//2) or (l == MAX_CELLS_PER_COL//2 + 1) or (k == i and l == j): 
						continue

					if (k, l) in liveCells:
						alive += 1

			if getCell(i, j) == ALIVE:
				if not((alive == 2) or (alive == 3)):
					gridCopy[i + MAX_CELLS_PER_ROW//2][j + MAX_CELLS_PER_COL//2] = DEAD
					liveCellsCopy.remove((i, j))
			else:
				if alive == 3:
					gridCopy[i + MAX_CELLS_PER_ROW//2][j + MAX_CELLS_PER_COL//2] = ALIVE
					liveCellsCopy.add((i, j))
	grid = pickle.loads(pickle.dumps(gridCopy))
	liveCells = pickle.loads(pickle.dumps(liveCellsCopy))

	# end = timer()

	#print(end - start)
def exit():
	pygame.quit()
	sys.exit()

init()

#just for testing
changeState(0,0)
changeState(1,1)
changeState(2,0)
changeState(2,1)
changeState(1,2)


while True:
	if(gameState == EDIT):
		edit()
	elif(gameState == RUN):
		update()
	pygame.display.update()
	mainClock.tick(1000)

exit()