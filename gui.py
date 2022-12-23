import pygame
import os
import sys
from itertools import *

from solver_utils.functions import *
from solver_utils.data import *
from gui_utils.functions import *
from gui_utils.data import *
from change_wd import *

change_wd()
pygame.init()

class Screen():
    def __init__(self, width, height, caption, FPS):
        self.width = width
        self.height = height
        self.caption = caption
        self.clock = pygame.time.Clock()
        self.FPS = FPS
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.icon = pygame.display.set_icon(pygame.image.load(os.path.join("gui_utils", "assets", "rubik_icon.ico")))
        pygame.display.set_caption(self.caption)

    def create_window(self):
        window = pygame.Surface((self.width, self.height))
        return window

screen = Screen(1000, 900, "RUBIK'S CUBE SOLVER", 60)
window = screen.create_window()

rects = [
[pygame.Rect(99, 230.2, 67, 67), pygame.Rect(166, 230.2, 67, 67), pygame.Rect(233, 230.2, 67, 67), pygame.Rect(99, 297.2, 67, 67), pygame.Rect(166, 297.2, 67, 67), pygame.Rect(233, 297.2, 67, 67), pygame.Rect(99, 364.2, 67, 67), pygame.Rect(166, 364.2, 67, 67), pygame.Rect(233, 364.2, 67, 67)],
[pygame.Rect(300, 230.2, 67, 67), pygame.Rect(367, 230.2, 67, 67), pygame.Rect(434, 230.2, 67, 67), pygame.Rect(300, 297.2, 67, 67), pygame.Rect(367, 297.2, 67, 67), pygame.Rect(434, 297.2, 67, 67), pygame.Rect(300, 364.2, 67, 67), pygame.Rect(367, 364.2, 67, 67), pygame.Rect(434, 364.2, 67, 67)],
[pygame.Rect(501, 230.2, 67, 67), pygame.Rect(568, 230.2, 67, 67), pygame.Rect(635, 230.2, 67, 67), pygame.Rect(501, 297.2, 67, 67), pygame.Rect(568, 297.2, 67, 67), pygame.Rect(635, 297.2, 67, 67), pygame.Rect(501, 364.2, 67, 67), pygame.Rect(568, 364.2, 67, 67), pygame.Rect(635, 364.2, 67, 67)],
[pygame.Rect(702, 230.2, 67, 67), pygame.Rect(769, 230.2, 67, 67), pygame.Rect(836, 230.2, 67, 67), pygame.Rect(702, 297.2, 67, 67), pygame.Rect(769, 297.2, 67, 67), pygame.Rect(836, 297.2, 67, 67), pygame.Rect(702, 364.2, 67, 67), pygame.Rect(769, 364.2, 67, 67), pygame.Rect(836, 364.2, 67, 67)],
[pygame.Rect(300, 29.2, 67, 67), pygame.Rect(367, 29.2, 67, 67), pygame.Rect(434, 29.2, 67, 67), pygame.Rect(300, 96.2, 67, 67), pygame.Rect(367, 96.2, 67, 67), pygame.Rect(434, 96.2, 67, 67), pygame.Rect(300, 163.2, 67, 67), pygame.Rect(367, 163.2, 67, 67), pygame.Rect(434, 163.2, 67, 67)],
[pygame.Rect(300, 431.2, 67, 67), pygame.Rect(367, 431.2, 67, 67), pygame.Rect(434, 431.2, 67, 67), pygame.Rect(300, 498.2, 67, 67), pygame.Rect(367, 498.2, 67, 67), pygame.Rect(434, 498.2, 67, 67), pygame.Rect(300, 565.2, 67, 67), pygame.Rect(367, 565.2, 67, 67), pygame.Rect(434, 565.2, 67, 67)]]

background = pygame.image.load(os.path.join("gui_utils", "assets", "background.png"))
solve_img_normal = pygame.transform.scale(pygame.image.load(os.path.join("gui_utils", "assets", "solve1.png")), (327, 58))
solve_img_clicking = pygame.transform.scale(pygame.image.load(os.path.join("gui_utils", "assets", "solve2.png")), (321, 53))
clear_img_normal = pygame.transform.scale(pygame.image.load(os.path.join("gui_utils", "assets", "clear1.png")), (243, 39))
clear_img_clicking = pygame.transform.scale(pygame.image.load(os.path.join("gui_utils", "assets", "clear2.png")), (238, 35))

button_solve = Button(window, 761, 760, solve_img_normal, solve_img_normal, solve_img_clicking)
button_clear = Button(window, 761, 827, clear_img_normal, clear_img_normal, clear_img_clicking)

def redraw_everything():
    screen.screen.blit(window, window.get_rect(bottomleft = screen.screen.get_rect().bottomleft))

def check_for_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.quit()
            pygame.joystick.quit()
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.mixer.quit()
                pygame.joystick.quit()
                pygame.quit()
                sys.exit()
                
run = True
while run:
    check_for_event()

    if button_solve.change() == True:
        try:
            moves = []
            moves, cube_map = solve_first_cross(cube_map, moves, centers_map, edges_map)
            moves, cube_map = solve_f2l(cube_map, moves, centers_map, edges_map, corners_map)
            moves, cube_map = solve_last_cross(cube_map, moves, 4, 1, "y")
            moves, cube_map = solve_oll(1, centers_map, cube_map, moves)
            moves, cube_map = solve_pll(cube_map, moves, "y", plls)
            moves = simplify(moves)
            
            print("moves:", end = " ")
            for i in moves:
                print(i, end=" ")

        except:
            print("ERROR: WRONG INPUT: cube is not solvable")    

    if button_clear.change() == True:
        cube_map = clear_cube_map(cube_map)

    select_color_picker(pickers)
    cube_map, initial_map = input_cube_map(cube_map, rects)

    window.blit(background, (0, 0))
    window = button_solve.redraw(window)
    window = button_clear.redraw(window)
    window = color_picker_redraw(pickers, window)
    window = fill_map(pickers, cube_map, rects, window)

    redraw_everything()
    pygame.display.update()
    screen.clock.tick(screen.FPS) 
