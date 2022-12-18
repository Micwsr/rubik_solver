import pygame
import random

from solver_utils.functions import *
from solver_utils.data import *

clock = pygame.time.Clock()
algo_tested = 0
algo_per_second = 0
multiples = 0
while True:
	cube_map = [
	[4, 4, 4, 4, 4, 4, 4, 4, 4],
	[2, 2, 2, 2, 2, 2, 2, 2, 2],
	[5, 5, 5, 5, 5, 5, 5, 5, 5],
	[3, 3, 3, 3, 3, 3, 3, 3, 3],
	[1, 1, 1, 1, 1, 1, 1, 1, 1],
	[0, 0, 0, 0, 0, 0, 0, 0, 0]]

	#Scramble the cube with a random sequence
	possible_moves = ["R", "R-", "L", "L-", "F", "F-", "B", "B-", "U", "U-", "D", "D-", "x", "x-", "y", "y-", "z", "z-"]
	test_algo = []
	len_test_algo = 10
	for i in range(len_test_algo):
		move_index = random.randint(0, len(possible_moves) - 1)
		test_algo.append(possible_moves[move_index])
	cube_map = move_algo(test_algo, cube_map)

	general_condition = False
	if cube_map == [[5, 5, 5, 2, 2, 5, 2, 2, 5], [0, 4, 4, 0, 4, 4, 0, 0, 0], [3, 3, 4, 3, 3, 4, 4, 4, 4], [1, 1, 1, 1, 5, 5, 1, 5, 5], [3, 3, 3, 3, 0, 0, 3, 0, 0], [2, 2, 2, 1, 1, 2, 1, 1, 2]]:
		general_condition = True

	algo_tested += 1
	algo_per_second += 1
	#result
	if general_condition == False:
		if pygame.time.get_ticks() % 1000 == 0:
			multiples += 1
			algo_per_second = algo_tested / multiples
			print(round(algo_per_second))
		print(test_algo)
		
	else:
		print(conditions)
		print(f"test_algo: \n {test_algo}")
		print(f"cube_map: \n {cube_map}")
		break
