import gui

EDIT = 0
RUN = 1

gameState = EDIT
liveCells = set()

def edit():
	global gameState
	
	x, y = 0, 0

	TAP_TIMER = 150
	
	r_time = l_time = u_time = d_time = cell_time = TAP_TIMER

	r_tap = l_tap =  u_tap = d_tap = cell_tap = True
	
	getTicksLastFrame = gui.pygame.time.get_ticks()

	while gameState == EDIT:

		t = gui.pygame.time.get_ticks()	
		dt = t - getTicksLastFrame
		getTicksLastFrame = t
		
		gui.pygame.event.pump()

		mb1 , mb3, mb2 = gui.pygame.mouse.get_pressed()

		if mb1:
		 	print(gui.pygame.mouse.get_pos())
		
		keys = gui.pygame.key.get_pressed()
		
		if not keys[gui.K_RIGHT]:
			if r_tap and r_time != TAP_TIMER:
				x += 1
			if not r_tap:
				r_tap = True
			x_dir = 0			
			r_time = TAP_TIMER

		if not keys[gui.K_LEFT]:
			if l_tap and l_time != TAP_TIMER:
				x -= 1
			if not l_tap:
				l_tap = True
			x_dir = 0			
			l_time = TAP_TIMER

		if not keys[gui.K_DOWN]:
			if d_tap and d_time != TAP_TIMER:
				y += 1
			if not d_tap:
				d_tap = True
			y_dir = 0			
			d_time = TAP_TIMER

		if not keys[gui.K_UP]:
			if u_tap and u_time != TAP_TIMER:
				y -= 1
			if not u_tap:
				u_tap = True
			y_dir = 0			
			u_time = TAP_TIMER  


		if keys[gui.K_RIGHT]:
			r_time -= dt
			if(r_time <= 0):
				r_time = TAP_TIMER
				r_tap = False
			x_dir = 1
		
		if keys[gui.K_LEFT]:
			l_time -= dt
			if(l_time <= 0):
				l_time = TAP_TIMER
				l_tap = False
			x_dir = -1
		
		if keys[gui.K_DOWN]:
			d_time -= dt
			if(d_time <= 0):
				d_time = TAP_TIMER
				d_tap = False
			y_dir = 1
		
		if keys[gui.K_UP]:
			u_time -= dt
			if(u_time <= 0):
				u_time = TAP_TIMER
				u_tap = False
			y_dir = -1
		
		if not keys[gui.K_s]:
			if cell_tap and cell_time != TAP_TIMER:
				gui.changeState(x, y)
			if not cell_tap:
				cell_tap = True			
			cell_time = TAP_TIMER

		if keys[gui.K_s]:
			cell_time -= dt
			if(cell_time <= 0):
				cell_time = TAP_TIMER
				cell_tap = False
		
		if keys[gui.K_SPACE] or keys[gui.K_RETURN]:
			gameState = RUN

		if keys[gui.K_ESCAPE]:
			gui.exit()

		if not r_tap or not l_tap:
			x += x_dir

		if not u_tap or not d_tap:
			y += y_dir

		if not cell_tap:
			gui.liveCells.add((x, y))
		
		if x <= -gui.CELLS_PER_ROW//2:
			x = -gui.CELLS_PER_ROW//2 + 1
		elif x >= +gui.CELLS_PER_ROW//2:
			x = gui.CELLS_PER_ROW//2
		if y <= -gui.CELLS_PER_COL//2:
			y = -gui.CELLS_PER_COL//2 + 1
		elif y >= gui.CELLS_PER_COL//2:
			y = gui.CELLS_PER_COL//2

		



		gui.drawGrid()
		gui.pygame.draw.rect(gui.windowSurface, gui.BLUE, gui.pygame.Rect((x + gui.CELLS_PER_ROW//2)* gui.CELL_SIZE, (y + gui.CELLS_PER_COL//2) * gui.CELL_SIZE, gui.CELL_SIZE, gui.CELL_SIZE), 2)
		gui.pygame.display.update()

		for event in gui.pygame.event.get():
			if event.type == gui.QUIT:
				gui.exit()