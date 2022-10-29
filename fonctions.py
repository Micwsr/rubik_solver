def input_map() -> list:
    print("")
    cube_map = []
    for i in range(6):
        cube_map.append(list(str(input(f"    face {i}: "))))
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

def rotate_facettes(face: int, prep_map: list, cube_map: list) -> list:     
    """takes moving elements of cube_map and place them differently in prep_map
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
    #flips only the face not the couronnne
    prep_map = create_prep_map()
    prep_map = rotate_facettes(face, prep_map, cube_map)
    cube_map = merge_maps(prep_map, cube_map)

    prep_map = create_prep_map()
    prep_map = rotate_facettes(face, prep_map, cube_map)
    cube_map = merge_maps(prep_map, cube_map)
    return cube_map

def rotate_couronne(face: int, prep_map: list, cube_map: list) -> list:
    """takes moving elements of cube_map and place them differently in prep_map
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

def rotate_face(face: int, cube_map: list) -> list:
    prep_map = create_prep_map()
    prep_map = rotate_facettes(face, prep_map, cube_map)
    prep_map = rotate_couronne(face, prep_map, cube_map)
    cube_map = merge_maps(prep_map, cube_map)
    return cube_map

def rotate_cube(axis: str, cube_map: list) -> list:
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

def merge_maps(prep_map: list, cube_map: list) -> list:
    """Takes the previously filled prep_map and fills the blanks elements with the cube_map elements
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
    
def create_prep_map() -> list:
    """Creates a new prep_map filled with ''
    """
    prep_map = []
    for i in range(6):
        prep_map.insert(i, [])
        for x in range(9):
            prep_map[i].insert(x, '')
    return prep_map
    
def change_map(cube_map):
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

def move(move: str, cube_map: list) -> list:
    """Returns the cube_map modified according to the move.
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
    for m in moves:
        cube_map = move(m, cube_map)
    return cube_map

#-------------------------------------------------------------------------------------------------------------

def place_center_down(color: int, centers_map: list, cube_map:list, moves: list) -> list:
    #centers
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
    right_edge = []
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
                    moves.extend(["L", "L", "U-", "F", "F"])
                    cube_map = move_algo(["L", "L", "U-", "F", "F"], cube_map)
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
                case 7:
                    pass
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
                    moves.extend(["U", "U", "R", "R"])
                    cube_map = move_algo(["U", "U", "R", "R"], cube_map)
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
                    moves.extend(["F", "L-", "U-", "L", "U", "U"])
                    cube_map = move_algo(["F", "L-", "U-", "L", "U", "U"], cube_map)
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