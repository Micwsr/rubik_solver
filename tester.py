#It scrambles the cube with a random sequence (test_algo)
#Then it solves the cube
#Finally it verifies if the cube was correctly solved, if so then it tries another one (infinite loop)
#If the cube wasn't correctly solved, it stops the loop and returns the test_algo
#Very useful to debug the program

import random
from solver_utils.functions import *
from solver_utils.data import *

total = 0
num = 0
while True:
	cube_map = [
	[4, 4, 4, 4, 4, 4, 4, 4, 4],
	[2, 2, 2, 2, 2, 2, 2, 2, 2],
	[5, 5, 5, 5, 5, 5, 5, 5, 5],
	[3, 3, 3, 3, 3, 3, 3, 3, 3],
	[1, 1, 1, 1, 1, 1, 1, 1, 1],
	[0, 0, 0, 0, 0, 0, 0, 0, 0]]
	moves = []

	#Scramble the cube with a random sequence
	possible_moves = ["R", "R-", "L", "L-", "F", "F-", "B", "B-", "U", "U-", "D", "D-", "x", "x-", "y", "y-", "z", "z-"]
	test_algo = []
	len_test_algo = 20
	for i in range(len_test_algo):
		move_index = random.randint(0, len(possible_moves) - 1)
		test_algo.append(possible_moves[move_index])
	cube_map = move_algo(test_algo, cube_map)

	#Solve the cube until f2l
	moves, cube_map = solve_first_cross(cube_map, moves, centers_map, edges_map)
	moves, cube_map = solve_f2l(cube_map, moves, centers_map, edges_map, corners_map)
	moves, cube_map = solve_last_cross(cube_map, moves, 4, 1, "y")
	moves, cube_map = solve_oll(1, centers_map, cube_map, moves)
	moves, cube_map = solve_pll(cube_map, moves, "y", plls)
	test_algo_string = ""
	for i in test_algo:
		test_algo_string += i
		test_algo_string += " "

	#verification
	condition = True
	for face in range(6):
		for facette in range(9):
			if cube_map[face][0] != cube_map[face][facette]:
				condition = False
	num += 1
	total += len(moves)
	if condition == True:
		print("TEST ALGO:", test_algo_string, end = "\r")
	else:
		print(f"\nTEST_ALGO: \n {test_algo}\n")
		print(f"CUBE_MAP: \n {cube_map}\n")
		print(f"MOVES: \n {moves}\n")
		break