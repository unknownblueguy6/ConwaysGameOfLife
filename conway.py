import pickle, platform, editor, gui
# from timeit import default_timer as timer

FPS = 60


def update():
	# start = timer()
	gui.drawGrid()
	
	liveCellsCopy = pickle.loads(pickle.dumps(gui.liveCells))
	
	checkedCells = set()

	for x, y in gui.liveCells:

		for i in range(x -1, x + 2):
			for j in range(y -1 , y +2):
			
				if (i, j) in checkedCells:
					continue

				alive = 0
			
				for k in range(i-1, i+2):
					for l in range(j-1, j+2):
						if(k == i and l == j): 	
							continue

						if (k, l) in gui.liveCells:
							alive += 1

				if (i, j) in gui.liveCells:
					if not((alive == 2) or (alive == 3)):
						liveCellsCopy.remove((i, j))
				else:
					if alive == 3:
						liveCellsCopy.add((i, j))
				checkedCells.add((i, j))

	gui.liveCells = pickle.loads(pickle.dumps(liveCellsCopy))

	# end = timer()

	#print(end - start)


gui.init()

while True:
	if(editor.gameState == editor.EDIT):
		editor.edit()
	if(editor.gameState == editor.RUN):
		update()
	for event in gui.pygame.event.get():
		if event.type == gui.QUIT:
			break
	gui.pygame.display.update()
	gui.mainClock.tick(FPS)

gui.exit()