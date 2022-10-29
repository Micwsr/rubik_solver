from utils import *
from fonctions import *

cube_map = input_map()

#first cross (white)
moves, cube_map = place_center_down(0, centers_map, cube_map, moves)

#try all arangements and see the shortest not only 2, 3, 4, 5 but also 3, 2, 5, 4,...
for color in range(2, 6):
	moves, cube_map = place_center_front(color, centers_map, cube_map, moves)
	moves, cube_map = place_edge(color, edges_map, cube_map, moves)

print("\nfirst white cross:")
print(f"    {moves}")
