import pygame
"""
cube_map: all pieces of the cube are referenced
ui map: the map of the cube in the ui
pickers: the colors pickers on the button left of the ui

"""

class Button:
	"The buttons can be in 3 different states: normal, mouse_on, clicking. For each state there's an image corresponding"
	"The buttons are created according to the size of each images given."
	"The x, y correspond to the middle of the button."
	def __init__(self, window, x, y, img_normal, img_mouse_on, img_clicking):
		self.window = window
		self.x = x
		self.y = y
		self.img_normal = img_normal
		self.img_mouse_on = img_mouse_on
		self.img_clicking = img_clicking
		self.img = self.img_normal
		self.surface = pygame.Surface((self.img.get_width(), self.img.get_height()))
		self.surface.blit(self.img, (0, 0))
		self.rect = self.img.get_rect(topleft = (self.x-self.img.get_width()/2, self.y-self.img.get_height()/2))

	def change(self):
		"Checks the mouse position and state, then changes the surface accordingly. Returns True if the button was just realized."
		launched = False
		x_mouse, y_mouse = pygame.mouse.get_pos()
		if self.img == self.img_clicking and pygame.mouse.get_pressed()[0] == False:
			launched = True
		
		if self.rect.collidepoint(x_mouse, y_mouse):
			self.img = self.img_mouse_on
			self.rect = self.img_mouse_on.get_rect(topleft = (self.x-self.img.get_width()/2, self.y-self.img.get_height()/2))
		
		if self.rect.collidepoint(x_mouse, y_mouse) == False:
			self.img = self.img_normal
			self.rect = self.img_normal.get_rect(topleft = (self.x-self.img.get_width()/2, self.y-self.img.get_height()/2))

		if pygame.mouse.get_pressed()[0] and pygame.Rect.collidepoint(self.rect, (x_mouse, y_mouse)):
			self.img = self.img_clicking
			self.rect = self.img_clicking.get_rect(topleft = (self.x-self.img.get_width()/2, self.y-self.img.get_height()/2))
		
		self.surface = pygame.transform.scale(self.surface, (self.img.get_width(), self.img.get_height()))
		self.surface.blit(self.img, (0, 0))
		return launched

	def redraw(self, window):
		"Draws the surface of the button on the window."
		window.blit(self.surface, (self.x-self.img.get_width()/2, self.y-self.img.get_height()/2))
		return window

class Picker:
	selected = -1
	def __init__(self, w, h, color, x, y, num):
		self.width = w
		self.height = h
		self.color = color
		self.x = x
		self.y = y
		self.surface = pygame.Surface((self.width, self.height))
		self.surface.fill(color)
		self.rect = self.surface.get_rect(topleft = (self.x, self.y))
		self.number = num

def clear_cube_map(cube_map):
	"Creates a new cube_map, it's called when the clear button is pressed"
	cube_map = [
	[-1, -1, -1, -1, -1, -1, -1, -1, -1],
	[-1, -1, -1, -1, -1, -1, -1, -1, -1],
	[-1, -1, -1, -1, -1, -1, -1, -1, -1],
	[-1, -1, -1, -1, -1, -1, -1, -1, -1],
	[-1, -1, -1, -1, -1, -1, -1, -1, -1],
	[-1, -1, -1, -1, -1, -1, -1, -1, -1]]
	return cube_map

def select_color_picker(pickers):
	"Checks if you click on a color picker, if so, then it changes the Picker.selected."
	x_mouse, y_mouse = pygame.mouse.get_pos()
	for picker in pickers:
		if picker.rect.collidepoint((x_mouse, y_mouse)) and pygame.mouse.get_pressed()[0]:
			Picker.selected = picker.number

def color_picker_redraw(pickers, window):
	"Redraws the color pickers only if they're not selected"
	for picker in pickers:
		if Picker.selected != picker.number:
			window.blit(picker.surface, picker.rect)
	return window

def input_cube_map(cube_map, rects):
    "Checks if the mouse is clicking on a facette of the ui map, if red is selected then it changes the cube_map accordingly."
    x_mouse, y_mouse = pygame.mouse.get_pos()
    y = 0
    for face in rects:
        x = 0
        for rect in face:
            if rect.collidepoint((x_mouse, y_mouse)) and pygame.mouse.get_pressed()[0]:
                cube_map[y].pop(x)
                cube_map[y].insert(x, Picker.selected)
            x += 1
        y += 1
    initial_map = cube_map
    return cube_map, initial_map

def fill_map(pickers, cube_map, rects, window):
    "Looks inside the cube_map, if there's something else than -1, then it fills the ui map"
    y = 0
    for face in cube_map:
        x = 0
        for element in face:
            if element != -1:
                window.blit(pickers[element].surface, rects[y][x])
            x += 1
        y += 1
    return window

def loading_bar(progress, total, bar_length, supplement):
    percent = progress/total*100
    num_bars = int(percent/100 * bar_length)
    progress_bars = ""
    for i in range(num_bars):
        progress_bars += "="
    small_bars = ""
    for i in range(bar_length - num_bars):
        small_bars += "-"

    print('\033[? 25l', end="")
    print(f"-|{progress_bars}{small_bars}|- {int(percent)}% | {progress}/{total} | {supplement}", end="\r")
    if progress == total:
        print("")