def input_map() -> list:
    """Console ui to get the layout of the cube. You can give: w (white), y (yellow), b (blue), g, r, o
    
    Returns:
        list: cube_map filled with letters.
    """
    print("")
    cube_map = []
    for i in range(6):
        cube_map.append(list(str(input(f"FACE {i}: "))))
    y = 0
    for face in cube_map:
        x = 0
        for i in face:
            match i:
                case "w":
                    cube_map[y].pop(x)
                    cube_map[y].insert(x, 0)
                case "y":
                    cube_map[y].pop(x)
                    cube_map[y].insert(x, 1)
                case "r":
                    cube_map[y].pop(x)
                    cube_map[y].insert(x, 2)
                case "o":
                    cube_map[y].pop(x)
                    cube_map[y].insert(x, 3)
                case "b":
                    cube_map[y].pop(x)
                    cube_map[y].insert(x, 4)
                case "g":
                    cube_map[y].pop(x)
                    cube_map[y].insert(x, 5)
            x += 1
        y += 1
    return cube_map

def change_map(cube_map: list) -> list:
    """Changes the cube_map filled with numbers to a cube_map filled with letters. Useful to get a more practical view of the cube_map in the console.
    
    Args:
        cube_map (list): Current layout of the cube.
    
    Returns:
        list: cube_map modified with letters instead of numbers.
    """

    y = 0
    for face in cube_map:
        x = 0
        for facette in face:
            match facette:
                case 0:
                    cube_map[y].pop(x)
                    cube_map[y].insert(x, "w")
                case 1:
                    cube_map[y].pop(x)
                    cube_map[y].insert(x, "y")
                case 2:
                    cube_map[y].pop(x)
                    cube_map[y].insert(x, "r")
                case 3:
                    cube_map[y].pop(x)
                    cube_map[y].insert(x, "o")
                case 4:
                    cube_map[y].pop(x)
                    cube_map[y].insert(x, "b")
                case 5:
                    cube_map[y].pop(x)
                    cube_map[y].insert(x, "g")
            x += 1
        y += 1
    for i in cube_map:
        print(i)

def create_prep_map() -> list:
    """Creates a new preparation map (prep_map) filled with blank strings.

    Returns:
        list: prep_map filled with the right number of elements, each element is a blank string.
    """
    
    prep_map = []
    for i in range(6):
        prep_map.insert(i, [])
        for x in range(9):
            prep_map[i].insert(x, '')
    return prep_map

def merge_maps(prep_map: list, cube_map: list) -> list:
    """Takes the previously filled prep_map and fills the blanks elements with the corresponding elements in the cube_map.

    Args:
        prep_map (list): The prep_map is filled only with the parts of the cube that changed place (other elements are blank strings.
        cube_map (list): Current layout of the cube.

    Returns:
        list: cube_map merged with the prep_map.
    """
    y = 0
    for face in prep_map:
        x = 0
        for case in face:
            if case == '':
                prep_map[y].pop(x)
                prep_map[y].insert(x, cube_map[y][x])
            x += 1
        y += 1
    
    cube_map = prep_map
    return cube_map

#----------------------------------------------------------------------------------------------------------#

def rotate_facettes(face: int, prep_map: list, cube_map: list) -> list:
    """Takes moving elements of cube_map and place them differently in prep_map according to the rotation. It's only rotating the face, not the couronne.
    
    Args:
        face (int): the face you want to turn (from 0 to 5)
        prep_map (list): same size as cube_map but filled with blank strings
    
    Returns:
        list: prep_map filled with the moving elements of the cube_map (others stay blank strings)
    """
    prep_map[face].pop(2)
    prep_map[face].insert(2, cube_map[face][0])
    prep_map[face].pop(8)
    prep_map[face].insert(8, cube_map[face][2])
    prep_map[face].pop(6)
    prep_map[face].insert(6, cube_map[face][8])
    prep_map[face].pop(0)
    prep_map[face].insert(0, cube_map[face][6])
        
    prep_map[face].pop(5)
    prep_map[face].insert(5, cube_map[face][1])
    prep_map[face].pop(7)
    prep_map[face].insert(7, cube_map[face][5])
    prep_map[face].pop(3)
    prep_map[face].insert(3, cube_map[face][7])
    prep_map[face].pop(1)
    prep_map[face].insert(1, cube_map[face][3])

    return prep_map
    
def flip_facettes(face: int, cube_map: list) -> list:
    """It does a 180° turn of the face, it doesn't rotate the couronne.
    
    Args:
        face (int): the face you want to flip
        cube_map (list): current layout of the cube

    Returns:
        list: cube_map with the face fliped (not the couronne)
    """
    prep_map = create_prep_map()
    prep_map = rotate_facettes(face, prep_map, cube_map)
    cube_map = merge_maps(prep_map, cube_map)

    prep_map = create_prep_map()
    prep_map = rotate_facettes(face, prep_map, cube_map)
    cube_map = merge_maps(prep_map, cube_map)
    return cube_map

def rotate_couronne(face: int, prep_map: list, cube_map: list) -> list:
    """It does a 90 degree turn of the couronne. It's not rotating the face.
    
    Args:
        face (int): the face you want to turn (from 0 to 5)
        prep_map (int): same size as cube_map but filled with blank strings
        cube_map (list): current layout of the cube

    Returns:
        list: cube_map modified with a 90° turn of the couronne of the given face
    """
    match face:
        case 0:
            prep_map[1].pop(0)
            prep_map[1].insert(0, cube_map[4][0])
            prep_map[1].pop(3)
            prep_map[1].insert(3, cube_map[4][3])
            prep_map[1].pop(6)
            prep_map[1].insert(6, cube_map[4][6])

            prep_map[5].pop(0)
            prep_map[5].insert(0, cube_map[1][0])
            prep_map[5].pop(3)
            prep_map[5].insert(3, cube_map[1][3])
            prep_map[5].pop(6)
            prep_map[5].insert(6, cube_map[1][6])

            prep_map[3].pop(2)
            prep_map[3].insert(2, cube_map[5][6])
            prep_map[3].pop(5)
            prep_map[3].insert(5, cube_map[5][3])
            prep_map[3].pop(8)
            prep_map[3].insert(8, cube_map[5][0])

            prep_map[4].pop(6)
            prep_map[4].insert(6, cube_map[3][2])
            prep_map[4].pop(3)
            prep_map[4].insert(3, cube_map[3][5])
            prep_map[4].pop(0)
            prep_map[4].insert(0, cube_map[3][8])

        case 1:
            prep_map[2].pop(0)
            prep_map[2].insert(0, cube_map[4][6])
            prep_map[2].pop(3)
            prep_map[2].insert(3, cube_map[4][7])
            prep_map[2].pop(6)
            prep_map[2].insert(6, cube_map[4][8])

            prep_map[5].pop(0)
            prep_map[5].insert(0, cube_map[2][6])
            prep_map[5].pop(1)
            prep_map[5].insert(1, cube_map[2][3])
            prep_map[5].pop(2)
            prep_map[5].insert(2, cube_map[2][0])

            prep_map[0].pop(2)
            prep_map[0].insert(2, cube_map[5][0])
            prep_map[0].pop(5)
            prep_map[0].insert(5, cube_map[5][1])
            prep_map[0].pop(8)
            prep_map[0].insert(8, cube_map[5][2])

            prep_map[4].pop(6)
            prep_map[4].insert(6, cube_map[0][8])
            prep_map[4].pop(7)
            prep_map[4].insert(7, cube_map[0][5])
            prep_map[4].pop(8)
            prep_map[4].insert(8, cube_map[0][2])            

        case 2:
            prep_map[4].pop(8)
            prep_map[4].insert(8, cube_map[1][8])
            prep_map[4].pop(5)
            prep_map[4].insert(5, cube_map[1][5])
            prep_map[4].pop(2)
            prep_map[4].insert(2, cube_map[1][2])

            prep_map[3].pop(0)
            prep_map[3].insert(0, cube_map[4][8])
            prep_map[3].pop(3)
            prep_map[3].insert(3, cube_map[4][5])
            prep_map[3].pop(6)
            prep_map[3].insert(6, cube_map[4][2])

            prep_map[5].pop(8)
            prep_map[5].insert(8, cube_map[3][0])
            prep_map[5].pop(5)
            prep_map[5].insert(5, cube_map[3][3])
            prep_map[5].pop(2)
            prep_map[5].insert(2, cube_map[3][6])

            prep_map[1].pop(2)
            prep_map[1].insert(2, cube_map[5][2])
            prep_map[1].pop(5)
            prep_map[1].insert(5, cube_map[5][5])
            prep_map[1].pop(8)
            prep_map[1].insert(8, cube_map[5][8])

        case 3:
            prep_map[4].pop(2)
            prep_map[4].insert(2, cube_map[2][8])
            prep_map[4].pop(1)
            prep_map[4].insert(1, cube_map[2][5])
            prep_map[4].pop(0)
            prep_map[4].insert(0, cube_map[2][2])

            prep_map[0].pop(0)
            prep_map[0].insert(0, cube_map[4][2])
            prep_map[0].pop(3)
            prep_map[0].insert(3, cube_map[4][1])
            prep_map[0].pop(6)
            prep_map[0].insert(6, cube_map[4][0])

            prep_map[5].pop(8)
            prep_map[5].insert(8, cube_map[0][6])
            prep_map[5].pop(7)
            prep_map[5].insert(7, cube_map[0][3])
            prep_map[5].pop(6)
            prep_map[5].insert(6, cube_map[0][0])

            prep_map[2].pop(8)
            prep_map[2].insert(8, cube_map[5][6])
            prep_map[2].pop(5)
            prep_map[2].insert(5, cube_map[5][7])
            prep_map[2].pop(2)
            prep_map[2].insert(2, cube_map[5][8])

        case 4:
            prep_map[0].pop(0)
            prep_map[0].insert(0, cube_map[1][0])
            prep_map[0].pop(1)
            prep_map[0].insert(1, cube_map[1][1])
            prep_map[0].pop(2)
            prep_map[0].insert(2, cube_map[1][2])

            prep_map[3].pop(0)
            prep_map[3].insert(0, cube_map[0][0])
            prep_map[3].pop(1)
            prep_map[3].insert(1, cube_map[0][1])
            prep_map[3].pop(2)
            prep_map[3].insert(2, cube_map[0][2])

            prep_map[2].pop(0)
            prep_map[2].insert(0, cube_map[3][0])
            prep_map[2].pop(1)
            prep_map[2].insert(1, cube_map[3][1])
            prep_map[2].pop(2)
            prep_map[2].insert(2, cube_map[3][2])

            prep_map[1].pop(0)
            prep_map[1].insert(0, cube_map[2][0])
            prep_map[1].pop(1)
            prep_map[1].insert(1, cube_map[2][1])
            prep_map[1].pop(2)
            prep_map[1].insert(2, cube_map[2][2])

        case 5:
            prep_map[2].pop(6)
            prep_map[2].insert(6, cube_map[1][6])
            prep_map[2].pop(7)
            prep_map[2].insert(7, cube_map[1][7])
            prep_map[2].pop(8)
            prep_map[2].insert(8, cube_map[1][8])

            prep_map[0].pop(6)
            prep_map[0].insert(6, cube_map[3][6])
            prep_map[0].pop(7)
            prep_map[0].insert(7, cube_map[3][7])
            prep_map[0].pop(8)
            prep_map[0].insert(8, cube_map[3][8])

            prep_map[3].pop(6)
            prep_map[3].insert(6, cube_map[2][6])
            prep_map[3].pop(7)
            prep_map[3].insert(7, cube_map[2][7])
            prep_map[3].pop(8)
            prep_map[3].insert(8, cube_map[2][8])

            prep_map[1].pop(6)
            prep_map[1].insert(6, cube_map[0][6])
            prep_map[1].pop(7)
            prep_map[1].insert(7, cube_map[0][7])
            prep_map[1].pop(8)
            prep_map[1].insert(8, cube_map[0][8])
    
    return prep_map

#----------------------------------------------------------------------------------------------------------#

def rotate_face(face: int, cube_map: list) -> list:
    """It does a 90 degree turn of the face and the couronne.
    
    Args:
        face (int): the face you want to turn (from 0 to 5)
        cube_map (list): current layout of the cube
    
    Returns:
        list: cube_map modified with the give face turned
    """
    prep_map = create_prep_map()
    prep_map = rotate_facettes(face, prep_map, cube_map)
    prep_map = rotate_couronne(face, prep_map, cube_map)
    cube_map = merge_maps(prep_map, cube_map)
    return cube_map

def rotate_cube(axis: str, cube_map: list) -> list:
    """It changes the cube_map according to the cube rotation given.
    
    Args: 
        axis (str): a rotation of the cube, it can be: x, y, z, x-, y-, z-
        cube_map (list): current layout of the cube

    Returns:
        list: the cube_map modified with the cube rotation given
    """
    match axis:
        case "x":
            faces = [2, 0]
            prep_map = create_prep_map()
            prep_map = rotate_facettes(faces[0], prep_map, cube_map)
            cube_map = merge_maps(prep_map, cube_map)
            
            prep_map = create_prep_map()
            prep_map = rotate_facettes(faces[1], prep_map, cube_map)
            cube_map = merge_maps(prep_map, cube_map)
            prep_map = create_prep_map()
            prep_map = rotate_facettes(faces[1], prep_map, cube_map)
            cube_map = merge_maps(prep_map, cube_map)
            prep_map = create_prep_map()
            prep_map = rotate_facettes(faces[1], prep_map, cube_map)
            cube_map = merge_maps(prep_map, cube_map)

            prep_map = create_prep_map()
            prep_map.pop(4)
            prep_map.insert(4, cube_map[1])
            prep_map.pop(3)
            prep_map.insert(3, cube_map[4])
            prep_map.pop(5)
            prep_map.insert(5, cube_map[3])
            prep_map.pop(1)
            prep_map.insert(1, cube_map[5])
            cube_map = merge_maps(prep_map, cube_map)

            cube_map = flip_facettes(3, cube_map)
            cube_map = flip_facettes(5, cube_map)

        case "y":

            faces = [4, 5]
            prep_map = create_prep_map()
            prep_map = rotate_facettes(faces[0], prep_map, cube_map)
            cube_map = merge_maps(prep_map, cube_map)
            
            prep_map = create_prep_map()
            prep_map = rotate_facettes(faces[1], prep_map, cube_map)
            cube_map = merge_maps(prep_map, cube_map)
            prep_map = create_prep_map()
            prep_map = rotate_facettes(faces[1], prep_map, cube_map)
            cube_map = merge_maps(prep_map, cube_map)
            prep_map = create_prep_map()
            prep_map = rotate_facettes(faces[1], prep_map, cube_map)
            cube_map = merge_maps(prep_map, cube_map)

            prep_map = create_prep_map()
            prep_map.pop(0)
            prep_map.insert(0, cube_map[1])
            prep_map.pop(3)
            prep_map.insert(3, cube_map[0])
            prep_map.pop(2)
            prep_map.insert(2, cube_map[3])
            prep_map.pop(1)
            prep_map.insert(1, cube_map[2])
            cube_map = merge_maps(prep_map, cube_map)

        case "z":
            faces = [1, 3]
            prep_map = create_prep_map()
            prep_map = rotate_facettes(faces[0], prep_map, cube_map)
            cube_map = merge_maps(prep_map, cube_map)
            
            prep_map = create_prep_map()
            prep_map = rotate_facettes(faces[1], prep_map, cube_map)
            cube_map = merge_maps(prep_map, cube_map)
            prep_map = create_prep_map()
            prep_map = rotate_facettes(faces[1], prep_map, cube_map)
            cube_map = merge_maps(prep_map, cube_map)
            prep_map = create_prep_map()
            prep_map = rotate_facettes(faces[1], prep_map, cube_map)
            cube_map = merge_maps(prep_map, cube_map)

            prep_map = create_prep_map()
            prep_map.pop(4)
            prep_map.insert(4, cube_map[0])
            prep_map.pop(2)
            prep_map.insert(2, cube_map[4])
            prep_map.pop(5)
            prep_map.insert(5, cube_map[2])
            prep_map.pop(0)
            prep_map.insert(0, cube_map[5])
            cube_map = merge_maps(prep_map, cube_map)

            prep_map = create_prep_map()
            prep_map = rotate_facettes(4, prep_map, cube_map)
            cube_map = merge_maps(prep_map, cube_map)
            prep_map = create_prep_map()
            prep_map = rotate_facettes(2, prep_map, cube_map)
            cube_map = merge_maps(prep_map, cube_map)
            prep_map = create_prep_map()
            prep_map = rotate_facettes(5, prep_map, cube_map)
            cube_map = merge_maps(prep_map, cube_map)
            prep_map = create_prep_map()
            prep_map = rotate_facettes(0, prep_map, cube_map)
            cube_map = merge_maps(prep_map, cube_map)
    
    return cube_map

def move(move: str, cube_map: list) -> list:
    """Changes the cube_map according the the given move. It can take only one move at a time.
    
    Args: 
        move (str): it can be: R, L, U, D, F, B, R-, L-, U-, D-, F-, B-, x, y, z, x-, y-, z-
        cube_map (list): Current layout of the cube.

    Returns:
        list: Layout of the cube after modification.
    """
    

    clock_wise = True
    for i in move:
        if i == "-":
            clock_wise = False

    if clock_wise:
        match move:
            case "L":
                face = 0
            case "F":
                face = 1
            case "R":
                face = 2
            case "B":
                face = 3
            case "U":
                face = 4
            case "D":
                face = 5  
            case "x":
                cube_map = rotate_cube(move, cube_map)
            case "y":
                cube_map = rotate_cube(move, cube_map)
            case "z":
                cube_map = rotate_cube(move, cube_map)

        if move != "x" and move != "y" and move != "z":
            cube_map = rotate_face(face, cube_map)
        
    else:
        match move:
            case "L-":
                face = 0
            case "F-":
                face = 1
            case "R-":
                face = 2
            case "B-":
                face = 3
            case "U-":
                face = 4
            case "D-":
                face = 5
            case "x-":
                for i in range(3):
                    cube_map = rotate_cube("x", cube_map)
            case "y-":
                for i in range(3):
                    cube_map = rotate_cube("y", cube_map)
            case "z-":
                for i in range(3):
                    cube_map = rotate_cube("z", cube_map)

        if move != "x-" and move != "y-" and move != "z-":
            for i in range(3):
                cube_map = rotate_face(face, cube_map)
    
    return cube_map

def move_algo(moves: list, cube_map: list) -> list:
    """Does the same as the move fonction but you can pass several moves (strings contained in a list).
    
    Args:
        moves (list): list of strings.
        cube_map (list): Current layout of the cube.
    
    Returns:
       list: Layout of the cube after modification.

    """
    for m in moves:
        cube_map = move(m, cube_map)
    return cube_map

#----------------------------------------------------------------------------------------------------------#

def place_center_down(color: int, centers_map: list, cube_map:list, moves: list) -> list:
    """Places the given color down.

    Args:
        color (int): color you want to place down
        centers_map (list): index of all centers in the cube_map
        cube_map (list): current layout of the cube
        moves (list): moves you need to do to solve the cube
    
    Returns:
        list: moves you need to do to solve the cube to which we added the moves to place the center down
        list: layout of the cube after modification
    """
    for centre in centers_map:
        if cube_map[centre[0]][centre[1]] == color:
            match centre[0]:
                case 0:
                    moves.append("z-")
                    cube_map = move("z-", cube_map)
                case 1:
                    moves.append("x-")
                    cube_map = move("x-", cube_map)
                case 2:
                    moves.append("z")
                    cube_map = move("z", cube_map)
                case 3:
                    moves.append("x")
                    cube_map = move("x", cube_map)
                case 4:
                    for i in range(2):
                        moves.append("x")
                        cube_map = move("x", cube_map)
                case 5:
                    pass
    return moves, cube_map

def place_center_front(color: int, centers_map: list, cube_map: list, moves: list) -> list:
    """Places the given color in front.

    Args:
        color (int): color you want to place to the front
        centers_map (list): index of all centers in the cube_map
        cube_map (list): current layout of the cube
        moves (list): moves you need to do to solve the cube
    
    Returns:
        list: moves you need to do to solve the cube to which we added the moves to place the center to the front
        list: layout of the cube after modification
    """    
    for centre in centers_map:
        if cube_map[centre[0]][centre[1]] == color:
            match centre[0]:
                case 0:
                    moves.append("y-")
                    cube_map = move("y-", cube_map)
                case 1:
                    pass
                case 2:
                    moves.append("y")
                    cube_map = move("y", cube_map)
                case 3:
                    for i in range(2):
                        moves.append("y")
                        cube_map = move("y", cube_map)
                case 4:
                    moves.append("x-")
                    cube_map = move("x-", cube_map)
                case 5:
                    moves.append("x")
                    cube_map = move("x", cube_map)
    return moves, cube_map

def place_edge(color: int, edges_map: list, cube_map: list, moves: list) -> list:    
    """PLace the right edge (white and given color) in the bottom front position. (The center of the given color must be in front, the white center must be down)
    
    Args:
        color (int): color of the right edge (white and color)
        edges_map (list): indexes of all edges in the cube_map
        cube_map (list): current layout of the cube
        moves (list): moves you need to do to solve the cube
    
    Returns:
        list: moves you need to do to solve the cube to which we added the moves to place the center in the front
        list: layout of the cube after modification 
    """
    for edge in edges_map:
        if cube_map[edge[0][0]][edge[0][1]] == color and cube_map[edge[1][0]][edge[1][1]] == 0:
            right_edge = [edge[0][0], edge[0][1]]
        if cube_map[edge[0][0]][edge[0][1]] == 0 and cube_map[edge[1][0]][edge[1][1]] == color:
            right_edge = [edge[1][0], edge[1][1]]

    match right_edge[0]:
        case 4:
            match right_edge[1]:
                case 1:
                    moves.extend(["U", "R-", "F", "R"])
                    cube_map = move_algo(["U", "R-", "F", "R"], cube_map)
                case 3:
                    moves.extend(["L", "F-", "L-"])
                    cube_map = move_algo(["L", "F-", "L-"], cube_map)
                case 5:
                    moves.extend(["R-", "F", "R"])
                    cube_map = move_algo(["R-", "F", "R"], cube_map)
                case 7:
                    moves.extend(["U-", "R-", "F", "R"])
                    cube_map = move_algo(["U-", "R-", "F", "R"], cube_map)
        case 0:
            match right_edge[1]:
                case 1:
                    moves.extend(["U-", "F", "F"])
                    cube_map = move_algo(["U-", "F", "F"], cube_map)
                case 3:
                    moves.extend(["L", "U-", "L-", "F", "F"])
                    cube_map = move_algo(["L", "U-", "L-", "F", "F"], cube_map)
                case 5:
                    moves.extend(["L-", "U-", "L", "F", "F"])
                    cube_map = move_algo(["L-", "U-", "L", "F", "F"], cube_map)
                case 7:
                    moves.extend(["L", "L", "U-", "L", "L", "F", "F"])
                    cube_map = move_algo(["L", "L", "U-", "L", "L", "F", "F"], cube_map)
        case 1:
            match right_edge[1]:
                case 1:
                    moves.extend(["F", "F"])
                    cube_map = move_algo(["F", "F"], cube_map)
                case 3:
                    moves.extend(["F-"])
                    cube_map = move_algo(["F-"], cube_map)
                case 5:
                    moves.extend(["F"])
                    cube_map = move_algo(["F"], cube_map)

        case 2:
            match right_edge[1]:
                case 1:
                    moves.extend(["U", "F", "F"])
                    cube_map = move_algo(["U", "F", "F"], cube_map)
                case 3:
                    moves.extend(["R", "U", "R-", "F", "F"])
                    cube_map = move_algo(["R", "U", "R-", "F", "F"], cube_map)
                case 5:
                    moves.extend(["R-", "U", "R", "F", "F"])
                    cube_map = move_algo(["R-", "U", "R", "F", "F"], cube_map)
                case 7:
                    moves.extend(["R", "R", "U", "F", "F"])
                    cube_map = move_algo(["R", "R", "U", "F", "F"], cube_map)
        case 3:
            match right_edge[1]:
                case 1:
                    moves.extend(["U", "U", "F", "F"])
                    cube_map = move_algo(["U", "U", "F", "F"], cube_map)
                case 3:
                    moves.extend(["R", "R", "F", "R", "R"])
                    cube_map = move_algo(["R", "R", "F", "R", "R"], cube_map)
                case 5:
                    moves.extend(["L", "L", "F-", "L", "L"])
                    cube_map = move_algo(["L", "L", "F-", "L", "L"], cube_map)
                case 7:
                    moves.extend(["B", "R", "R", "F", "R", "R", "B-"])
                    cube_map = move_algo(["B", "R", "R", "F", "R", "R", "B-"], cube_map)
        case 5:
            match right_edge[1]:
                case 1:
                    moves.extend(["F", "L-", "U-", "L", "F", "F"])
                    cube_map = move_algo(["F", "L-", "U-", "L", "F", "F"], cube_map)
                case 3:
                    moves.extend(["L-", "F-", "L"])
                    cube_map = move_algo(["L-", "F-", "L"], cube_map)
                case 5:
                    moves.extend(["R", "F", "R-"])
                    cube_map = move_algo(["R", "F", "R-"], cube_map)
                case 7:
                    moves.extend(["B", "B", "U", "U", "B", "B", "R", "U-", "R-", "F"])
                    cube_map = move_algo(["B", "B", "U", "U", "B", "B", "R", "U-", "R-", "F"], cube_map)
    return moves, cube_map

def find_corner(corners_map: list, cube_map: list, color_0: int, color_1: int, color_2: int) -> dict:
    """Finds the position of the right corner in the cube_map, according to the 3 given colors.

    Args:
        corners_map (list): indexes of all corners in the cube_map
        cube_map (list): current layout of the cube
        color_0 (int): first color
        color_1 (int): second color
        color_2 (int): third color

    Returns:
        dict: contains the right corner position in the cube_map, contains "color_0", "color_1", "color_2"
    """
    right_corner = []
    for corner in corners_map:
        for facette in corner:
            if cube_map[facette[0]][facette[1]] == color_0:
                right_corner.append(corner)
    prep_right_corner = []
    for corner in right_corner:
        for facette in corner:
            if cube_map[facette[0]][facette[1]] == color_1:
                prep_right_corner.append(corner)
    right_corner = prep_right_corner
    prep_right_corner = []
    for corner in right_corner:
        for facette in corner:
            if cube_map[facette[0]][facette[1]] == color_2:
                prep_right_corner.append(corner)
    for corner in prep_right_corner:
        right_corner = corner
    prep_right_corner = {}
    for facette in right_corner:
        if cube_map[facette[0]][facette[1]] == color_0:
            prep_right_corner.update({"color_0": facette})
        elif cube_map[facette[0]][facette[1]] == color_1:
            prep_right_corner.update({"color_1": facette})
        elif cube_map[facette[0]][facette[1]] == color_2:
            prep_right_corner.update({"color_2": facette})
    right_corner  = prep_right_corner
    del prep_right_corner
    return right_corner

def find_edge(edges_map: list, cube_map: list, color_1: int, color_2: int) -> dict:
    """Find the right edge in the cube_map according to the 2 give colors,

    Args:
        edges_map (list): indexes of all edges in the cube_map
        cube_map (list): current layout of the cube
        color_1 (int): will be in front
        color_2 (int): will be in the right

    Returns:
        dict: contains the right edge position in the cube_map
    """    
    for edge in edges_map:
        if cube_map[edge[0][0]][edge[0][1]] == color_1 and cube_map[edge[1][0]][edge[1][1]] == color_2:
            right_edge = {"color_1": edge[0], "color_2": edge[1]} 
        if cube_map[edge[0][0]][edge[0][1]] == color_2 and cube_map[edge[1][0]][edge[1][1]] == color_1:
            right_edge = {"color_1": edge[1], "color_2": edge[0]}
    return right_edge

def place_f2l(cube_map: list, moves: list, corners_map: list, edges_map: list, color_0: int, color_1: int, color_2: int) -> list:
    """Places one F2L according to the 3 given colors.

    Args:
        cube_map (list): current layout of the cube
        moves (list): moves you need to do to solve the cube
        corners_map (list): indexes of all corner in the cube_map
        edges_map (list): indexes of all edges in the cube_map
        color_0 (int): will be in the bottom position of the corner
        color_1 (int): will be in front position of the corner
        color_2 (int): will be in the right position of the corner

    Returns:
        list, list: moves you need to complete, layout of the cube after modification
    """    
    movement = []
    right_corner = find_corner(corners_map, cube_map, color_0, color_1, color_2)
    
    #places corner to the top right position
    if right_corner["color_1"] == [1, 0] or right_corner["color_1"] == [0, 2] or right_corner["color_1"] == [4, 6]:
            movement.extend(["U-"])
    elif right_corner["color_1"] == [4, 0] or right_corner["color_1"] == [0, 0] or right_corner["color_1"] == [3, 2]:
        movement.extend(["U", "U"])
    elif right_corner["color_1"] == [4, 2] or right_corner["color_1"] == [2, 2] or right_corner["color_1"] == [3, 0]:
        movement.extend(["U"])
    elif right_corner["color_1"] == [1, 8] or right_corner["color_1"] == [2, 6] or right_corner["color_1"] == [5, 2]:
        if right_corner["color_0"] != [5, 2]:
            movement.extend(["R", "U", "R-", "U-"])   
    elif right_corner["color_1"] == [1, 6] or right_corner["color_1"] == [0, 8] or right_corner["color_1"] == [5, 0]:
        movement.extend(["L-", "U-", "L"])    
    elif right_corner["color_1"] == [5, 6] or right_corner["color_1"] == [0, 6] or right_corner["color_1"] == [3, 8]:
        movement.extend(["L", "U-", "U-", "L-"])    
    elif right_corner["color_1"] == [5, 8] or right_corner["color_1"] == [2, 8] or right_corner["color_1"] == [3, 6]:
        movement.extend(["R-", "U", "U", "R", "U-"])
    
    moves.extend(movement)
    cube_map = move_algo(movement, cube_map)
    movement = []

    #find the right corner
    right_corner = find_corner(corners_map, cube_map, color_0, color_1, color_2)

    #Place the corner
    match right_corner["color_0"]:
        case [1, 2]:
            movement = ["F-", "U-", "F"]
        case [4, 8]:
            movement = ["R", "U", "U", "R-", "U-", "R", "U", "R-"]
        case [2, 0]:
            movement = ["R", "U", "R-"]
    
    moves.extend(movement)
    cube_map = move_algo(movement, cube_map)
    movement = []

    #find the right edge
    right_edge = find_edge(edges_map, cube_map, color_1, color_2)
    match right_edge["color_1"]:
        case [4, 7]:
            movement = ["U", "U", "F-", "U", "F", "U", "R", "U-", "R-"]
        case [1, 1]:
            movement = ["U", "R", "U-", "R-", "U-", "F-", "U", "F"]
        case [4, 3]:
            movement = ["U", "F-", "U", "F", "U", "R", "U-", "R-"]
        case [0, 1]:
            movement = ["R", "U-", "R-", "U-", "F-", "U", "F"]
        case [4, 1]:
            movement = ["F-", "U", "F", "U", "R", "U-", "R-"]
        case [3, 1]:
            movement = ["U-", "R", "U-", "R-", "U-", "F-", "U", "F"]
        case [4, 5]:
            movement = ["U-", "F-", "U", "F", "U", "R", "U-", "R-"]
        case [2, 1]:
            movement = ["U", "U", "R", "U-", "R-", "U-", "F-", "U", "F"]
        
        case [1, 3]:
            movement = ["L-", "U-", "L", "U", "F", "U", "F-", "F-", "U", "F", "U", "R", "U-", "R-"]
        case [0, 5]:
            movement = ["L-", "U-", "L", "U", "F", "U", "F-", "U-", "R", "U-", "R-", "U-", "F-", "U", "F"]
        case [0, 3]:
            movement = ["L", "U-", "L-", "U-", "B-", "U", "B", "U", "R", "U-", "R-", "U-", "F-", "U", "F"]
        case [3, 5]:
            movement = ["L", "U-", "L-", "U-", "B-", "U", "B", "U", "U", "F-", "U", "F", "U", "R", "U-", "R-"]
        case [3, 3]:
            movement = ["B", "U", "B-", "U-", "R-", "U-", "R", "R", "U-", "R-", "U-", "F-", "U", "F"]
        case [2, 5]:
            movement = ["B", "U", "B-", "U-", "R-", "U-", "R", "U", "F-", "U", "F", "U", "R", "U-", "R-"] 
        case [2, 3]:
            movement = ["R", "U-", "R-", "U", "y-", "R-", "U", "U", "R", "U", "U", "R-", "U", "R"]
    
    
    cube_map = move_algo(movement, cube_map)
    moves.extend(movement)
    return moves, cube_map

#----------------------------------------------------------------------------------------------------------#

def solve_first_cross(cube_map: list, moves: list, centers_map: list, edges_map: list) -> list:
    """Solves the first cross.

    Args:
        cube_map (list): current layout of the cube
        moves (list): moves you need to do to solve the cube
        centers_map (list): indexes of all centers in the cube_map
        edges_map (list): indexes of all edges in the cube_map

    Returns:
        list, list: moves you need to complete, layout of the cube after modification
    """    
    moves, cube_map = place_center_down(0, centers_map, cube_map, moves)

    colors = [2, 5, 3, 4]
    for color in colors:
        moves, cube_map = place_center_front(color, centers_map, cube_map, moves)
        moves, cube_map = place_edge(color, edges_map, cube_map, moves)
    
    return moves, cube_map

def solve_f2l(cube_map: list, moves: list, centers_map: list, edges_map: list, corners_map: list) -> list:
    """Solves the first two layers by solving them one after another (using: place_f2l function).

    Args:
        cube_map (list): current layout of the cube
        moves (list): moves you need to do to solve the cube
        centers_map (list): indexes of all centers in the cube_map
        edges_map (list): indexes of all edges in the cube_map
        corners_map (list): indexes of all corners in the cube_map

    Returns:
        list, list: moves you need to complete, layout of the cube after modification
    """ 
    corner_colors = [
    [0, 4, 2],
    [0, 2, 5],
    [0, 5, 3],
    [0, 3, 4]]

    for color in corner_colors:
        moves, cube_map = place_center_front(color[1], centers_map, cube_map, moves)
        moves, cube_map = place_f2l(cube_map, moves, corners_map, edges_map, color[0], color[1], color[2])
    
    return moves, cube_map

def solve_last_cross(cube_map: list, moves: list, face: int, last_color: int, axis_of_rotation: str) -> list:
    """Solves the last cross.

    Args:
        cube_map (list): current layout of the cube
        moves (list): moves you need to do to solve the cube
        face (int): face you want to solve the last cross of (from 0 to 5)
        last_color (int): color you want to solve the last cross of (from 0 to 5)
        axis_of_rotaiton (str): axis corresponding to the face.

    Returns:
        list, list: moves you need to complete, layout of the cube after modification
    """
    facette_position = [1, 3, 4, 5, 7]
    cross_state = []
    for i in facette_position:
        if cube_map[face][i] == last_color:
            cross_state.append([face, i])
    movement = []
    found = False
    while found == False:
        match cross_state: 
            case [[4, 4]]:
                movement = ["R", "U", "U", "R", "R", "F", "R", "F-", "U", "U", "R-", "F", "R", "F-"]
                found = True
            case [[4, 1], [4, 4], [4, 5]]:
                movement = ["L", "U", "F", "U-", "F-", "L-"]
                found = True
            case [4, 3], [4, 4], [4, 5]:
                movement = ["R-", "F", "R", "U", "R-", "U-", "F-", "U", "R"]
                found = True
            case [4, 1], [4, 3], [4, 4], [4, 5], [4, 7]:
                found = True 
            case other:
                moves.append(axis_of_rotation)
                cube_map = rotate_cube(axis_of_rotation, cube_map)
                cross_state = []
                for i in facette_position:
                    if cube_map[face][i] == last_color:
                        cross_state.append([face, i])
    cube_map = move_algo(movement, cube_map)
    moves.extend(movement)
    return moves, cube_map

def solve_oll(color: list, centers_map: list, cube_map: list, moves: list) -> list:
    """Solves the OLL.

    Args:
        color (int): the color of the face you want to solve the oll of (from 0 to 5), the face you want to solve must be at the top before solving
        centers_map (list): indexes of all centers in the cube_map
        cube_map (list): current layout of the cube
        moves (list): moves you need to do to solve the cube

    Returns:
        list, list: moves you need to complete, layout of the cube after modification
    """
    match color:
        case 2:
            color_down = 3
        case 3:
            color_down = 2
        case 0:
            color_down = 1
        case 1:
            color_down = 0
        case 4:
            color_down = 5
        case 5:
            color_down = 4
    moves, cube_map = place_center_down(color_down, centers_map, cube_map, moves)
    

    found = False
    movements = []
    while found == False:
        #find each facette position of the last color
        color_positions = []
        y = 0
        for face in cube_map:
            x = 0
            for facette in face:
                if facette == color:
                    color_positions.append([y, x])
                x += 1
            y += 1

        #each OLL case (57), if it doesn't exist, then it rotates the cube y to and tries again
        match color_positions:
            #OLL CROSS
            case [0, 0], [1, 0], [2, 0], [4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [4, 7]:
                movements.extend(["R", "U", "U", "R-", "U-", "R", "U-", "R-"])
                found = True
            case [1, 2], [2, 2], [3, 2], [4, 1], [4, 3], [4, 4], [4, 5], [4, 6], [4, 7]:
                movements.extend(["R", "U", "R-", "U", "R", "U", "U", "R-"])
                found = True
            case [1, 0], [1, 2], [3, 0], [3, 2], [4, 1], [4, 3], [4, 4], [4, 5], [4, 7]:
                movements.extend(["R", "U", "U", "R-", "U-", "R", "U", "R-", "U-", "R", "U-", "R-"])
                found = True
            case [0, 0], [0, 2], [1, 2], [3, 0], [4, 1], [4, 3], [4, 4], [4, 5], [4, 7]:
                movements.extend(["R", "U", "U", "R", "R", "U-", "R", "R", "U-", "R", "R", "U", "U", "R"])
                found = True
            case [1, 0], [3, 2], [4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [4, 7], [4, 8]:
                movements.extend(["y", "R", "U", "R", "D", "R-", "U-", "R", "D-", "R", "R"])
                found = True
            case [1, 0], [2, 2], [4, 0], [4, 1], [4, 3], [4, 4], [4, 5], [4, 7], [4, 8]:
                movements.extend(["x", "R-", "U", "R", "D-", "R-", "U-", "R", "D", "x-"])
                found = True
            case [1, 0], [1, 2], [4, 0], [4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [4, 7]:
                movements.extend(["y", "y", "R", "R", "D-", "R", "U", "U", "R-", "D", "R", "U", "U", "R"])
                found = True
            case [4, 0], [4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [4, 6], [4, 7], [4, 8]:
                found = True

            case [1, 0], [1, 1], [3, 1], [3, 2], [4, 2], [4, 3], [4, 4], [4, 5], [4, 8]:
                movements .extend(["R", "U", "R-", "U-", "R-", "F", "R", "F-"])
                found = True
            case [0, 0], [0, 2], [1, 1], [3, 1], [4, 2], [4, 3], [4, 4], [4, 5], [4, 8]:
                movements.extend(["F", "R", "U", "R-", "U-", "F-"])
                found = True

            case [0, 1], [0, 2], [2, 2], [3, 1], [3, 2], [4, 4], [4, 5], [4, 7], [4, 8]:
                movements.extend(["L-", "x-", "U", "U", "R", "U", "R-", "U", "L", "x"])
                found = True
            case [0, 1], [0, 2], [1, 0], [1, 1], [2, 0], [4, 1], [4, 2], [4, 4], [4, 5]:
                movements.extend(["L", "x", "U", "U", "R-", "U-", "R", "U-", "L-", "x-"])
                found = True
            
            case other:
                cube_map = rotate_cube("y", cube_map)
                moves.append("y")

    moves.extend(movements)
    cube_map = move_algo(movements, cube_map)
    
    return moves, cube_map

def solve_pll(cube_map: list, moves: list, axis_of_rotation: str, plls: list) -> list:
    """Solves the PLL. (Tries each pll until it finds the right one)

    Args:
        cube_map (list): current layout of the cube
        moves (list): moves you need to do to solve the cube
        axis_of_rotation (str): axis perpendicular to the pll you want to solve ("y")
        pll (list): all pll formulas

    Returns:
        list, list: moves you need to complete, layout of the cube after modification
    """
    condition = True
    for i in cube_map[5]:
        if i != 0:
            condition = False
    for i in cube_map[4]:
        if i != 1:
            condition = False
    facettes = [3, 4, 5, 6, 7, 8]
    for i in range(4):
        for x in facettes:
            if cube_map[i][3] != cube_map[i][x]:
                condition = False
    facettes = [0, 1, 2]
    for face in range(4):
        for facette in facettes:
            if cube_map[face][0] != cube_map[face][facette]:
                condition = False

    if condition == False:
        for pll in plls:
            cube_map_copy = cube_map.copy()
            rotations = []
            for i in range(4):
                #try a pll
                cube_map_copy = move_algo(pll, cube_map_copy)
                
                #verification if it's the right one
                condition = True
                for i in cube_map_copy[5]:
                    if i != 0:
                        condition = False
                for i in cube_map_copy[4]:
                    if i != 1:
                        condition = False
                facettes = [3, 4, 5, 6, 7, 8]
                for i in range(4):
                    for x in facettes:
                        if cube_map_copy[i][3] != cube_map_copy[i][x]:
                            condition = False
                facettes = [0, 1, 2]
                for i in range(4):
                    for x in facettes:
                        if cube_map_copy[i][0] != cube_map_copy[i][x]:
                            condition = False

                if condition == False:
                    rotations.append(axis_of_rotation)
                    cube_map_copy = cube_map.copy()
                    cube_map_copy = move_algo(rotations, cube_map_copy)
                else:
                    movements = []
                    movements.extend(rotations)
                    movements.extend(pll)
                    break
            if condition == True:
                break

        moves.extend(movements)
        cube_map = move_algo(movements, cube_map)
    moves, cube_map = turn_last_face(cube_map, moves, "U")
    return moves, cube_map

def turn_last_face(cube_map: list, moves: list, face_to_rotate: int) -> list:
    """Turns the last face to solve the cube (sometimes the pll doesn't solve completely, one move is missing)

    Args:
        cube_map (list): current layout of the cube
        moves (list): moves you need to do to solve the cube
        face_to_rotate (int): from 0 to 5

    Returns:
        list, list: moves you need to complete, layout of the cube after modification
    """
    cube_map_copy = cube_map.copy()
    rotations = []
    found = False
    while found == False:
        cube_map = move(face_to_rotate, cube_map)
        rotations.append(face_to_rotate)
        condition = True
        for face in range(6):
            for facette in range(9):
                if cube_map[face][0] != cube_map[face][facette]:
                    condition = False
        if condition:
            found = True

    match len(rotations):
        case 3:
            rotations = ["U-"]
        case 4:
            rotations = []

    moves.extend(rotations)
    cube_map = cube_map_copy
    cube_map = move_algo(rotations, cube_map)
    return moves, cube_map

def solve_first_cross_anagram(cube_map: list, moves: list) -> list:
    "Not used, Solves the first cross, checks different possibilities and returns the shortest"
    moves_possibles = []
    colors_all = [2, 5, 3, 4]
    second_map = cube_map
    for colors in itertools.permutations(colors_all):
        moves = []
        colors = list(colors)
        moves, second_map = place_center_down(0, centers_map, second_map, moves)
        for color in colors:
            moves, second_map = place_center_front(color, centers_map, second_map, moves)
            moves, second_map = place_edge(color, edges_map, second_map, moves)
        moves_possibles.append(moves)
        second_map = cube_map

    #simplify all possible moves then find the shortest
    moves = min(moves_possibles, key=len)
    cube_map = move_algo(moves, cube_map)
    return moves, cube_map

def simplify(moves: list) -> list:
    """Remove all unnecessary moves, return a list of moves simplified.

    Args:
        moves (list): moves you need to do to complete the cube

    Returns:
        list: simplified version of the given moves list
    """    
    #remove 4 consecutive moves
    for i in range(len(moves)-3):
        if moves[i] == moves[i+1] == moves[i+2] == moves[i+3]:
            for x in range(4):
                moves.pop(i+x)
                moves.insert(i+x, 0)

    moves_copy = []           
    for move in moves:
        if move != 0:
            moves_copy.append(move)
            moves = moves_copy
	
	#renove 3 consecutive moves
    for i in range(len(moves)-2):
        if moves[i] == moves[i+1] == moves[i+2]:
            moves[i] += "-"
            moves[i+1] = 0
            moves[i+2] = 0
	
    moves_copy = []           
    for move in moves:
        if move != 0:
            moves_copy.append(move)
            moves = moves_copy
	
	#remove 2 opposite moves
    moves_copy = moves.copy()
    for i in range(len(moves)-1):
        containing = [False, False]
        for x in moves[i]:
            if x == "-":
                containing[0] = True
        for x in moves[i+1]:
            if x == "-":
                containing[1] = True
    no_sign = []
    for x in moves[i]:
        if x != "-":
            no_sign.append(x)
    for x in moves[i+1]:
        if x != "-":
            no_sign.append(x)
    if (containing[0] == (not containing[1])) and (no_sign[0] == no_sign[1]):
        moves[i] = 0
        moves[i+1] = 0
		
    moves_copy = []           
    for move in moves:
        if move != 0:
            moves_copy.append(move)
    moves = moves_copy
    del moves_copy, containing, no_sign
    #remove all cube rotations
    return moves
