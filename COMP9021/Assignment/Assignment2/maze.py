'''
This program is for COMP9021 Assignment 2.
Written by Jingyun Shen.
Example interaction:

>>> from maze import *
>>> maze = Maze('maze_1.txt')
>>> maze.analyse()
The maze has 12 gates.
The maze has 8 sets of walls that are all connected.
The maze has 2 inaccessible inner points.
The maze has 4 accessible areas.
The maze has 3 sets of accessible cul-de-sacs that are all connected.
The maze has a unique entry-exit path with no intersection not to cul-de-sacs.
>>> maze.display()

'''

import sys

def find_gates(maze_array):
    gates = 0
    row = len(maze_array)
    column = len(maze_array[0])

    for i in range(column - 1):
        if maze_array[0][i] == 0 or maze_array[0][i] == 2:
            gates += 1
    for i in range(column - 1):
        if maze_array[row - 1][i] == 0 or maze_array[row - 1][i] == 2:
            gates += 1
    for i in range(row - 1):
        if maze_array[i][0] == 0 or maze_array[i][0] == 1:
            gates += 1
    for i in range(row - 1):
        if maze_array[i][column - 1] == 0 or maze_array[i][column - 1] == 1:
            gates += 1
            
    return gates

def find_set_of_walls(maze_array):
    set_of_walls = 0
    row = len(maze_array)
    column = len(maze_array[0])
    visited = [[False for _ in range(column)] for _ in range(row)]

    def find_walls(maze_array, row, column, i, j):
        if (maze_array[i][j] == 1 or maze_array[i][j] == 3) and j < column - 1 \
           and (not visited[i][j + 1]):
            visited[i][j] = True
            visited[i][j + 1] = True
            find_walls(maze_array, row, column, i, j + 1)
        if (maze_array[i][j] == 2 or maze_array[i][j] == 3) and i < row - 1 \
           and (not visited[i + 1][j]):
            visited[i][j] = True
            visited[i + 1][j] = True
            find_walls(maze_array, row, column, i + 1, j)
        if (maze_array[i][j - 1] == 1 or maze_array[i][j - 1] == 3) and j > 0 \
           and (not visited[i][j - 1]):
            visited[i][j] = True
            visited[i][j - 1] = True
            find_walls(maze_array, row, column, i, j - 1)
        if (maze_array[i - 1][j] == 2 or maze_array[i - 1][j] == 3) and i > 0 \
           and (not visited[i - 1][j]):
            visited[i][j] = True
            visited[i - 1][j] = True
            find_walls(maze_array, row, column, i - 1, j)
        return
    
    for i in range(row):
        for j in range(column):
            if maze_array[i][j] and (not visited[i][j]):
                find_walls(maze_array, row, column, i, j)
                set_of_walls += 1
    
    return set_of_walls

def inside_analyse(maze_array):
    inaccessible_inner_points = 0
    accessible_areas = 0
    row = len(maze_array)
    column = len(maze_array[0])

    # find all gates
    all_gates = []
    for i in range(column - 1):
        if maze_array[0][i] == 0 or maze_array[0][i] == 2:
            all_gates.append([0, i + 0.5])
    for i in range(column - 1):
        if maze_array[row - 1][i] == 0 or maze_array[row - 1][i] == 2:
            all_gates.append([row - 1, i + 0.5])
    for i in range(row - 1):
        if maze_array[i][0] == 0 or maze_array[i][0] == 1:
            all_gates.append([i + 0.5, 0])
    for i in range(row - 1):
        if maze_array[i][column - 1] == 0 or maze_array[i][column - 1] == 1:
            all_gates.append([i + 0.5, column - 1])
    accessible_areas = len(all_gates)
    
    visited = dict()
    for i in range(row - 1):
        for j in range(column - 1):
            visited[(i + 0.5, j + 0.5)] = False
    
    def if_left(x, y):
        if maze_array[int(x - 0.5)][int(y - 0.5)] == 2 or \
           maze_array[int(x - 0.5)][int(y - 0.5)] == 3:
            return False
        else:
            return True

    def if_right(x, y):
        if maze_array[int(x - 0.5)][int(y + 0.5)] == 2 or \
           maze_array[int(x - 0.5)][int(y + 0.5)] == 3:
            return False
        else:
            return True
        
    def if_down(x, y):
        if maze_array[int(x + 0.5)][int(y - 0.5)] == 1 or \
           maze_array[int(x + 0.5)][int(y - 0.5)] == 3:
            return False
        else:
            return True

    def if_up(x, y):
        if maze_array[int(x - 0.5)][int(y - 0.5)] == 1 or \
           maze_array[int(x - 0.5)][int(y - 0.5)] == 3:
            return False
        else:
            return True
        
       
    def find_areas(x, y, start_gate):
        visited[(x, y)] = True
        if if_left(x, y):
            #print("allow left at", [x, y])
            if y > 0.5 and (not visited[(x, y - 1)]):
                visited[(x, y - 1)] = True
                #print('visited', x, y-1) #####
                find_areas(x, y - 1, start_gate)
            if y == 0.5 and (not start_gate == [x, 0]):
                all_gates.remove([x, 0])
        if if_right(x, y):
            #print("allow right at", [x, y])
            if y < column - 1.5 and (not visited[(x, y + 1)]):
                visited[(x, y + 1)] = True
                #print('visited', x, y+1) #####
                find_areas(x, y + 1, start_gate)
            if y == column - 1.5 and (not start_gate == [x, column - 1]):
                all_gates.remove([x, column - 1])
        if if_up(x, y):
            #print("allow up at", [x, y])
            if x > 0.5 and (not visited[(x - 1, y)]):
                visited[(x - 1, y)] = True
                #print('visited', x-1, y) #####
                find_areas(x - 1, y, start_gate)
            if x == 0.5 and (not start_gate == [0, y]):
                all_gates.remove([0, y])
        if if_down(x, y):
            #print("allow down at", [x, y])
            if x < row - 1.5 and (not visited[(x + 1, y)]):
                visited[(x + 1, y)] = True
                #print('visited', x+1, y) #####
                find_areas(x + 1, y, start_gate)
            if x == row - 1.5 and (not start_gate == [row - 1, y]):
                all_gates.remove([row - 1, y])
        return 
    
    for each_gate in all_gates:
        if each_gate[0] == 0:
            find_areas(each_gate[0] + 0.5, each_gate[1], each_gate)
        elif each_gate[0] == row - 1:
            find_areas(each_gate[0] - 0.5, each_gate[1], each_gate)
        elif each_gate[1] == 0:
            find_areas(each_gate[0], each_gate[1] + 0.5, each_gate)
        elif each_gate[1] == column - 1:
            find_areas(each_gate[0], each_gate[1] - 0.5, each_gate)
    accessible_areas = len(all_gates)

    inaccessbile_points_array = []
    for points in visited:
        if not visited[points]:
            inaccessible_inner_points += 1
            inaccessbile_points_array.append(points)

    output = [inaccessible_inner_points, accessible_areas, inaccessbile_points_array]
    return output

def scan(row, column, points, degree, edges, cul_de_sacs_array):
    length = len(points)
    keep_scanning = False

    for i in range(length):
        if degree[i] == 3:
            cur_point = points[i]
            if edges[i][0] == False:
                edges[i][0] = True
                degree[i] += 1
                cul_de_sacs_array.append((points[i][0], points[i][1]))
                if cur_point[0] > 0.5:
                    mod_point = [cur_point[0] - 1, cur_point[1]]
                    idx = points.index(mod_point)
                    edges[idx][1] = True
                    degree[idx] += 1
                    
            if edges[i][1] == False:
                edges[i][1] = True
                degree[i] += 1
                cul_de_sacs_array.append((points[i][0], points[i][1]))
                if cur_point[0] < row - 1.5:
                    mod_point = [cur_point[0] + 1, cur_point[1]]
                    idx = points.index(mod_point)
                    edges[idx][0] = True
                    degree[idx] += 1

            if edges[i][2] == False:
                edges[i][2] = True
                degree[i] += 1
                cul_de_sacs_array.append((points[i][0], points[i][1]))
                if cur_point[1] > 0.5:
                    mod_point = [cur_point[0], cur_point[1] - 1]
                    idx = points.index(mod_point)
                    edges[idx][3] = True
                    degree[idx] += 1

            if edges[i][3] == False:
                edges[i][3] = True
                degree[i] += 1
                cul_de_sacs_array.append((points[i][0], points[i][1]))
                if cur_point[1] < column - 1.5:
                    mod_point = [cur_point[0], cur_point[1] + 1]
                    idx = points.index(mod_point)
                    edges[idx][2] = True
                    degree[idx] += 1    

    for i in range(length):
        if degree[i] == 3:
            keep_scanning = True
            break
        
    return keep_scanning
   
def find_cul_de_sacs(maze_array, inaccessbile_points_array, cul_de_sacs_array):
    cul_de_sacs = 0
    row = len(maze_array)
    column = len(maze_array[0])
    points = [] # point[(row, column)]
    degree = [] # degree[0,1,2,3,4]
    edges = []  # edges[[up, down, left, right]]
    all_gates = []
    ini_degree = []
    visited = dict()
    
    for i in range(row - 1):
        for j in range(column - 1):
            points.append([i + 0.5, j + 0.5])
            degree.append(0)
            edges.append([False, False, False, False])
            visited[(i + 0.5, j + 0.5)] = False
            
    # find all gates
    for i in range(column - 1):
        if maze_array[0][i] == 0 or maze_array[0][i] == 2:
            all_gates.append([0, i + 0.5])
    for i in range(column - 1):
        if maze_array[row - 1][i] == 0 or maze_array[row - 1][i] == 2:
            all_gates.append([row - 1, i + 0.5])
    for i in range(row - 1):
        if maze_array[i][0] == 0 or maze_array[i][0] == 1:
            all_gates.append([i + 0.5, 0])
    for i in range(row - 1):
        if maze_array[i][column - 1] == 0 or maze_array[i][column - 1] == 1:
            all_gates.append([i + 0.5, column - 1])
                
    # initialize edges[]
    for i in range(row):
        for j in range(column):
            if maze_array[i][j] == 1:
                if i > 0:
                    idx = points.index([i - 0.5, j + 0.5])
                    edges[idx][1] = True
                if i < row - 1:
                    idx = points.index([i + 0.5, j + 0.5])
                    edges[idx][0] = True
            if maze_array[i][j] == 2:
                if j < column - 1:
                    idx = points.index([i + 0.5, j + 0.5])
                    edges[idx][2] = True
                if j > 0:
                    idx = points.index([i + 0.5, j - 0.5])
                    edges[idx][3] = True
            if maze_array[i][j] == 3:
                if i > 0:
                    idx = points.index([i - 0.5, j + 0.5])
                    edges[idx][1] = True
                if i < row - 1:
                    idx = points.index([i + 0.5, j + 0.5])
                    edges[idx][0] = True
                if j < column - 1:
                    idx = points.index([i + 0.5, j + 0.5])
                    edges[idx][2] = True
                if j > 0:
                    idx = points.index([i + 0.5, j - 0.5])
                    edges[idx][3] = True
                    
    # initialize degree[]
    for i in range(len(points)):
        tmp = 0
        for j in range(4):
            if edges[i][j]:
                tmp += 1
        degree[i] = tmp
    
    for i in range(len(degree)):
        ini_degree.append(degree[i])
        
    # scan and modify
    keep_scanning = scan(row, column, points, degree, edges, cul_de_sacs_array)
    while keep_scanning:
        keep_scanning = scan(row, column, points, degree, edges, cul_de_sacs_array)
        
    def if_left(x, y):
        if maze_array[int(x - 0.5)][int(y - 0.5)] == 2 or \
           maze_array[int(x - 0.5)][int(y - 0.5)] == 3:
            return False
        else:
            return True
        
    def if_left_now(x, y):
        idx = points.index([x, y])
        if not edges[idx][2]:
            return True
        else:
            return False
        
    def if_right(x, y):
        if maze_array[int(x - 0.5)][int(y + 0.5)] == 2 or \
           maze_array[int(x - 0.5)][int(y + 0.5)] == 3:
            return False
        else:
            return True
        
    def if_right_now(x, y):
        idx = points.index([x, y])
        if not edges[idx][3]:
            return True
        else:
            return False
        
    def if_down(x, y):
        if maze_array[int(x + 0.5)][int(y - 0.5)] == 1 or \
           maze_array[int(x + 0.5)][int(y - 0.5)] == 3:
            return False
        else:
            return True

    def if_down_now(x, y):
        idx = points.index([x, y])
        if not edges[idx][1]:
            return True
        else:
            return False

    def if_up(x, y):
        if maze_array[int(x - 0.5)][int(y - 0.5)] == 1 or \
           maze_array[int(x - 0.5)][int(y - 0.5)] == 3:
            return False
        else:
            return True

    def if_up_now(x, y):
        idx = points.index([x, y])
        if not edges[idx][0]:
            return True
        else:
            return False
        
    # enter from gates 
    def find_areas(x, y, start_gate, cul_de_sacs):
        visited[(x, y)] = True
        
        if if_left_now(x, y):
            if y > 0.5 and (not visited[(x, y - 1)]):
                visited[(x, y - 1)] = True               
                cul_de_sacs = find_areas(x, y - 1, start_gate, cul_de_sacs)
            if y == 0.5 and (not start_gate == [x, 0]):
                all_gates.remove([x, 0])
        else:
            if if_left(x, y):
                cul_de_sacs += 1       
                
        if if_right_now(x, y):
            if y < column - 1.5 and (not visited[(x, y + 1)]):
                visited[(x, y + 1)] = True
                cul_de_sacs = find_areas(x, y + 1, start_gate, cul_de_sacs)
            if y == column - 1.5 and (not start_gate == [x, column - 1]):
                all_gates.remove([x, column - 1])
        else:
            if if_right(x, y):
                cul_de_sacs += 1
                
        if if_up_now(x, y):
            if x > 0.5 and (not visited[(x - 1, y)]):
                visited[(x - 1, y)] = True
                cul_de_sacs = find_areas(x - 1, y, start_gate, cul_de_sacs)
            if x == 0.5 and (not start_gate == [0, y]):
                all_gates.remove([0, y])
        else:
            if if_up(x, y):
                cul_de_sacs += 1
                
        if if_down_now(x, y):
            if x < row - 1.5 and (not visited[(x + 1, y)]):
                visited[(x + 1, y)] = True
                cul_de_sacs = find_areas(x + 1, y, start_gate, cul_de_sacs)
            if x == row - 1.5 and (not start_gate == [row - 1, y]):
                all_gates.remove([row - 1, y])
        else:
            if if_down(x, y):
                cul_de_sacs += 1
            
        return cul_de_sacs   

    for each_gate in all_gates:
        if each_gate[0] == 0:
            if not if_up_now(each_gate[0] + 0.5, each_gate[1]):
                cul_de_sacs += 1
            else:
                cul_de_sacs = find_areas(each_gate[0] + 0.5, each_gate[1], each_gate, cul_de_sacs)
        elif each_gate[0] == row - 1:
            if not if_down_now(each_gate[0] - 0.5, each_gate[1]):
                cul_de_sacs += 1
            else:
                cul_de_sacs = find_areas(each_gate[0] - 0.5, each_gate[1], each_gate, cul_de_sacs)
        elif each_gate[1] == 0:
            if not if_left_now(each_gate[0], each_gate[1] + 0.5):
                cul_de_sacs += 1
            else:
                cul_de_sacs = find_areas(each_gate[0], each_gate[1] + 0.5, each_gate, cul_de_sacs)
        elif each_gate[1] == column - 1:
            if not if_right_now(each_gate[0], each_gate[1] - 0.5):
                cul_de_sacs += 1
            else:
                cul_de_sacs = find_areas(each_gate[0], each_gate[1] - 0.5, each_gate, cul_de_sacs)

    for each_point in cul_de_sacs_array:
        if each_point in inaccessbile_points_array:
            cul_de_sacs_array.remove(each_point)
                     
    return [cul_de_sacs, degree, edges]

def find_entry_exit_path(maze_array, degree, edges):
    entry_exit_path = 0
    all_gates = []
    points = []
    row = len(maze_array)
    column = len(maze_array[0])
    visited = dict()
    
    for i in range(row - 1):
        for j in range(column - 1):
            points.append([i + 0.5, j + 0.5])
            visited[(i + 0.5, j + 0.5)] = False
            
    # find all gates
    for i in range(column - 1):
        if maze_array[0][i] == 0 or maze_array[0][i] == 2:
            all_gates.append([0, i + 0.5])
    for i in range(column - 1):
        if maze_array[row - 1][i] == 0 or maze_array[row - 1][i] == 2:
            all_gates.append([row - 1, i + 0.5])
    for i in range(row - 1):
        if maze_array[i][0] == 0 or maze_array[i][0] == 1:
            all_gates.append([i + 0.5, 0])
    for i in range(row - 1):
        if maze_array[i][column - 1] == 0 or maze_array[i][column - 1] == 1:
            all_gates.append([i + 0.5, column - 1])
        
    def if_left_now(x, y):
        idx = points.index([x, y])
        if not edges[idx][2]:
            return True
        else:
            return False
        
    def if_right_now(x, y):
        idx = points.index([x, y])
        if not edges[idx][3]:
            return True
        else:
            return False

    def if_down_now(x, y):
        idx = points.index([x, y])
        if not edges[idx][1]:
            return True
        else:
            return False

    def if_up_now(x, y):
        idx = points.index([x, y])
        if not edges[idx][0]:
            return True
        else:
            return False
        
    # remove some gates
    for each_gate in all_gates:
        if each_gate[0] == 0:
    
            if not if_up_now(each_gate[0] + 0.5, each_gate[1]):
                
                all_gates.remove(each_gate)
        if each_gate[0] == row - 1:
            
            if not if_down_now(each_gate[0] - 0.5, each_gate[1]):
                
                all_gates.remove(each_gate)
        if each_gate[1] == 0:
            
            if not if_left_now(each_gate[0], each_gate[1] + 0.5):
                
                all_gates.remove(each_gate)
        if each_gate[1] == column - 1:
            
            if not if_right_now(each_gate[0], each_gate[1] - 0.5):
                
                all_gates.remove(each_gate)
                
    for each_gate in all_gates:
        
        if each_gate[0] == 0:
            
            if not if_up_now(each_gate[0] + 0.5, each_gate[1]):
                
                all_gates.remove(each_gate)
        if each_gate[0] == row - 1:
            
            if not if_down_now(each_gate[0] - 0.5, each_gate[1]):
                
                all_gates.remove(each_gate)
        if each_gate[1] == 0:
           
            if not if_left_now(each_gate[0], each_gate[1] + 0.5):
                
                all_gates.remove(each_gate)
        if each_gate[1] == column - 1:
         
            if not if_right_now(each_gate[0], each_gate[1] - 0.5):
             
                all_gates.remove(each_gate)            
    
    # enter from each gate
    path_gates = []
    def find_areas(x, y, start_gate):
        visited[(x, y)] = True
        direction = 0
        out = True
        if if_left_now(x, y):
            direction += 1
            if y > 0.5 and (not visited[(x, y - 1)]):
                visited[(x, y - 1)] = True
                out = find_areas(x, y - 1, start_gate)
                if not out:
                    return False
            if y == 0.5 and (not start_gate == [x, 0]):
                all_gates.remove([x, 0])
                
        if if_right_now(x, y):
            direction += 1
            if y < column - 1.5 and (not visited[(x, y + 1)]):
                visited[(x, y + 1)] = True
                out = find_areas(x, y + 1, start_gate)
                if not out:
                    return False
            if y == column - 1.5 and (not start_gate == [x, column - 1]):
                all_gates.remove([x, column - 1])
                
        if if_up_now(x, y):
            direction += 1
            if x > 0.5 and (not visited[(x - 1, y)]):
                visited[(x - 1, y)] = True
                out = find_areas(x - 1, y, start_gate)
                if not out:
                    return False
            if x == 0.5 and (not start_gate == [0, y]):
                all_gates.remove([0, y])
                
        if if_down_now(x, y):
            direction += 1
            if x < row - 1.5 and (not visited[(x + 1, y)]):
                visited[(x + 1, y)] = True
                out = find_areas(x + 1, y, start_gate)
                if not out:
                    return False
            if x == row - 1.5 and (not start_gate == [row - 1, y]):
                all_gates.remove([row - 1, y])
                
        if direction > 2:
            out = False
        else:
            out = True

        return out

    new_visited = dict()
    for i in range(row - 1):
        for j in range(column - 1):
            new_visited[(i + 0.5, j + 0.5)] = False
            
    def find_path_gates(x, y, start_gate):
        #print(f'{x}, {y}:  left-{if_left_now(x, y)}, right-{if_right_now(x, y)}, up-{if_up_now(x, y)}, down-{if_down_now(x, y)}')
        new_visited[(x, y)] = True
        path_gates[-1].append([x, y])
        
        if if_left_now(x, y):
             
            if y > 0.5 and (not new_visited[(x, y - 1)]):
                new_visited[(x, y - 1)] = True
                #path_gates[-1].append('left')
                #path_gates[-1].append([x, y])
                find_path_gates(x, y - 1, start_gate)
            if y == 0.5 and (not start_gate == [x, 0]):
                path_gates[-1].append([x, -0.5])
                
        if if_right_now(x, y):
             
            if y < column - 1.5 and (not new_visited[(x, y + 1)]):
                #path_gates[-1].append('right')
                new_visited[(x, y + 1)] = True
                #path_gates[-1].append([x, y])
                find_path_gates(x, y + 1, start_gate)
            if y == column - 1.5 and (not start_gate == [x, column - 1]):
                path_gates[-1].append([x, column - 0.5])
                
        if if_up_now(x, y):
        
            if x > 0.5 and (not new_visited[(x - 1, y)]):
                #path_gates[-1].append('up')
                new_visited[(x - 1, y)] = True
                #path_gates[-1].append([x, y])
                find_path_gates(x - 1, y, start_gate)
            
            if x == 0.5 and (not start_gate == [0, y]):
                path_gates[-1].append([-0.5, y])
                
        if if_down_now(x, y):
            
            if x < row - 1.5 and (not new_visited[(x + 1, y)]):
                #path_gates[-1].append('down')
                new_visited[(x + 1, y)] = True
                #path_gates[-1].append([x, y])
                find_path_gates(x + 1, y, start_gate)
            if x == row - 1.5 and (not start_gate == [row - 1, y]):
                path_gates[-1].append([row - 0.5, y])
        return
    
    for each_gate in all_gates:
        if each_gate[0] == 0:
            if find_areas(each_gate[0] + 0.5, each_gate[1], each_gate):
                #print(f'{each_gate[0] + 0.5, each_gate[1]}')
                entry_exit_path += 1
                path_gates.append([[each_gate[0] - 0.5, each_gate[1]]])
                find_path_gates(each_gate[0] + 0.5, each_gate[1], each_gate)
                #path_gates.append(each_gate)
        elif each_gate[0] == row - 1:
            if find_areas(each_gate[0] - 0.5, each_gate[1], each_gate):
                #print(f'{each_gate[0] - 0.5, each_gate[1]}')
                entry_exit_path += 1
                path_gates.append([[each_gate[0] + 0.5, each_gate[1]]])
                find_path_gates(each_gate[0] - 0.5, each_gate[1], each_gate)
                #path_gates.append(each_gate)
        elif each_gate[1] == 0:
            if find_areas(each_gate[0], each_gate[1] + 0.5, each_gate):
                #print(f'{each_gate[0], each_gate[1] + 0.5}')
                entry_exit_path += 1
                path_gates.append([[each_gate[0], each_gate[1] - 0.5]])
                find_path_gates(each_gate[0], each_gate[1] + 0.5, each_gate)
                #path_gates.append(each_gate)
        elif each_gate[1] == column - 1:
            if find_areas(each_gate[0], each_gate[1] - 0.5, each_gate):
                #print(f'{each_gate[0], each_gate[1] - 0.5}')
                entry_exit_path += 1
                path_gates.append([[each_gate[0], each_gate[1] + 0.5]])
                find_path_gates(each_gate[0], each_gate[1] - 0.5, each_gate)
                #path_gates.append(each_gate)
                
    #print('path gate: ', path_gates ) #####              
    return [entry_exit_path, path_gates]

class MazeError(Exception):
    pass

class Maze:
    def __init__(self, filename = 'maze.txt'):
        self.file = filename
        self.name = filename[:-4]
        # Create self.maze_array
        try:
            f = open(self.file, 'r')
        except FileNotFoundError:
            print('Error! File cannot found in current directory.')
            sys.exit()
            
        file_array = []
        with open(self.file) as maze_file:
            for line in maze_file:
                each_line = list(filter(None, line.split(' ')))
                file_array.append(each_line)
 
        
        while ['\n'] in file_array:
            file_array.remove(['\n'])

        if len(file_array[-1]) == 0:
            file_array = file_array[:-1]          
                  
        self.maze_array = []   
        for i in range(len(file_array)):
            self.maze_array.append([])
            for j in range(len(file_array[i])):
                if file_array[i][j].endswith('\n'):
                    file_array[i][j] = file_array[i][j][:-1]
                    
                if file_array[i][j] == '':
                    file_array[i].remove('')
                    continue

                for each_str in file_array[i][j]:
                    if each_str >= '0' and each_str <= '9':
                        self.maze_array[i].append(int(each_str))
                    else:
                        self.maze_array[i].append(each_str)
                        
    
        '''
        self.maze_array = []
        print(file_array)###
        for i in range(len(file_array)):
            self.maze_array.append([])
            for j in range(len(file_array[i])):
                tmp = str(file_array[i][j])
                if len(tmp) > 1:
                    for each_str in tmp:
                        self.maze_array[i].append(int(each_str))
                else:
                    self.maze_array[i].append(int(tmp))
 '''                   
        
        self.maze_array = []
        represent_maze_error = 0
        for i in range(len(file_array)):
            self.maze_array.append([])
            for j in range(len(file_array[i])):
                tmp = str(file_array[i][j])
                if len(tmp) > 1:
                    for each_str in tmp:
                        if int(each_str) == 0 or int(each_str) == 1 \
                            or int(each_str) == 2 or int(each_str) == 3:
                            self.maze_array[i].append(int(each_str))
                        else:
                                
                            raise MazeError('Incorrect input.')
                else:
                    if int(tmp) == 0 or int(tmp) == 1 \
                        or int(tmp) == 2 or int(tmp) == 3:
                        self.maze_array[i].append(int(tmp))
                    else:
                        raise MazeError('Incorrect input.')
        if len(self.maze_array) < 2 or len(self.maze_array) > 31:
            raise MazeError('Incorrect input.')
                 
        for i in range(len(self.maze_array)):
            if not len(self.maze_array[i]) == len(self.maze_array[0]):
                raise MazeError('Incorrect input.')
            if self.maze_array[i][-1] == 1 or self.maze_array[i][-1] == 3:
                represent_maze_error = 1
                raise MazeError('Input does not represent a maze.')
        for j in range(len(self.maze_array[-1])):
            if self.maze_array[-1][j] == 2 or self.maze_array[-1][j] == 3:
                represent_maze_error = 1
                raise MazeError('Input does not represent a maze.')

        f.close()
        self.cul_de_sacs_array = []
        
    def analyse(self):
        gates = find_gates(self.maze_array)
        set_of_walls = find_set_of_walls(self.maze_array)
        output = inside_analyse(self.maze_array)
        inaccessible_inner_points = output[0]
        accessible_areas = output[1]
        inaccessbile_points_array = output[2]
        output1 = find_cul_de_sacs(self.maze_array, inaccessbile_points_array, self.cul_de_sacs_array)
        cul_de_sacs = output1[0]
        degree = output1[1]
        edges = output1[2]
        output2 = find_entry_exit_path(self.maze_array, degree, edges)
        entry_exit_path = output2[0]
        #print(sorted(self.cul_de_sacs_array))
        if gates == 0:
            print('The maze has no gate.')
        elif gates == 1:
            print('The maze has a single gate.')
        else:
            print(f'The maze has {gates} gates.')

        if set_of_walls == 0:
            print('The maze has no walls.')
        elif set_of_walls == 1:
            print('The maze has walls that are all connected.')
        else:
            print(f'The maze has {set_of_walls} sets of walls that are all connected.')

        if inaccessible_inner_points == 0:
            print('The maze has no inaccessible inner point.')
        elif inaccessible_inner_points == 1:
            print('The maze has a unique inaccessible inner point.')
        else:
            print(f'The maze has {inaccessible_inner_points} inaccessible inner points.')

        if accessible_areas == 0:
            print('The maze has no accessible area.')
        elif accessible_areas == 1:
            print('The maze has a unique accessible area.')
        else:
            print(f'The maze has {accessible_areas} accessible areas.')

        if cul_de_sacs == 0:
            print('The maze has no accessible cul-de-sacs.')
        elif cul_de_sacs == 1:
            print('The maze has accessible cul-de-sacs that are all connected.')
        else:
            print(f'The maze has {cul_de_sacs} sets of accessible cul-de-sacs that are all connected.')

        if entry_exit_path == 0:
            print('The maze has no entry-exit path with no intersection not to cul-de-sacs.')
        elif entry_exit_path == 1:
            print('The maze has a unique entry-exit path with no intersection not to cul-de-sacs.')
        else:
            print(f'The maze has {entry_exit_path} entry-exit paths with no intersections not to cul-de-sacs.')
    
        
    def display(self):
        new_file = open(self.name + '.tex', 'w')
        new_file.write('\\documentclass[10pt]{article}\n')
        new_file.write('\\usepackage{tikz}\n')
        new_file.write('\\usetikzlibrary{shapes.misc}\n')
        new_file.write('\\usepackage[margin=0cm]{geometry}\n')
        new_file.write('\\pagestyle{empty}\n')
        new_file.write('\\tikzstyle{every node}=[cross out, draw, red]\n')
        new_file.write('\n')
        new_file.write('\\begin{document}\n')
        new_file.write('\n')
        new_file.write('\\vspace*{\\fill}\n')
        new_file.write('\\begin{center}\n')
        new_file.write('\\begin{tikzpicture}[x=0.5cm, y=-0.5cm, ultra thick, blue]\n')
        new_file.write('% Walls\n')

        # display all the walls
        for i in range(len(self.maze_array)):
            j = 0
            while j < len(self.maze_array[i]):
                if self.maze_array[i][j] == 1 or self.maze_array[i][j] == 3:
                    if j == len(self.maze_array[i]) - 1:
                        new_file.write(f'    \\draw ({j},{i}) -- ({j + 1},{i});\n')
                        j += 1
                    elif self.maze_array[i][j + 1] == 1 or self.maze_array[i][j + 1] == 3:
                        temp = j
                        j += 1 
                        while self.maze_array[i][j] == 1 or self.maze_array[i][j] == 3:
                            j += 1
                        new_file.write(f'    \\draw ({temp},{i}) -- ({j},{i});\n')
                    else:
                        new_file.write(f'    \\draw ({j},{i}) -- ({j + 1},{i});\n')
                        j += 1
                else:
                    j += 1
                    
        row = len(self.maze_array)
        col = len(self.maze_array[0])
        for i in range(col):
            j = 0
            while j < row:
                if self.maze_array[j][i] == 2 or self.maze_array[j][i] == 3:
                    if j == row - 1:
                        new_file.write(f'    \\draw ({i},{j}) -- ({i},{j + 1});\n')
                        j += 1
                    elif self.maze_array[j + 1][i] == 2 or self.maze_array[j + 1][i] == 3:
                        temp = j
                        j += 1
                        while self.maze_array[j][i] == 2 or self.maze_array[j][i] == 3:
                            j += 1
                        new_file.write(f'    \\draw ({i},{temp}) -- ({i},{j});\n')
                    else:
                        new_file.write(f'    \\draw ({i},{j}) -- ({i},{j + 1});\n')
                        j += 1
                else:
                    j += 1

        # display the points
        new_file.write('% Pillars\n')
        row = len(self.maze_array)
        column = len(self.maze_array[0])
        visited = [[False for _ in range(column)] for _ in range(row)]

        for i in range(row):
            for j in range(column):
                if self.maze_array[i][j] == 1:
                    visited[i][j] = True
                    visited[i][j + 1] = True
                if self.maze_array[i][j] == 2:
                    visited[i][j] = True
                    visited[i + 1][j] = True
                if self.maze_array[i][j] == 3:
                    visited[i][j] = True
                    visited[i][j + 1] = True
                    visited[i + 1][j] = True

        for i in range(row):
            for j in range(column):
                if not visited[i][j]:
                    new_file.write(f'    \\fill[green] ({j},{i}) circle(0.2);\n')

        # display the cul_de_sacs
        output = inside_analyse(self.maze_array)
        inaccessible_inner_points = output[0]
        accessible_areas = output[1]
        inaccessbile_points_array = output[2]
        out = find_cul_de_sacs(self.maze_array, inaccessbile_points_array, self.cul_de_sacs_array)
        degree = out[1]
        edges = out[2]
        self.cul_de_sacs_array = sorted(self.cul_de_sacs_array)
        new_file.write('% Inner points in accessible cul-de-sacs\n')
        for i in range(len(self.cul_de_sacs_array)):
            new_file.write(f'    \\node at ({self.cul_de_sacs_array[i][1]},{self.cul_de_sacs_array[i][0]}) {{}};\n')

        # display the paths
        out1 = find_entry_exit_path(self.maze_array, degree, edges)
        path_gates = out1[1]
        
        new_path_gates = []
        for i in range(len(path_gates)):
            j = 1
            while j < len(path_gates[i]):
                if j < len(path_gates[i]) - 1 and path_gates[i][j - 1][0] == path_gates[i][j][0] and \
                                   path_gates[i][j + 1][0] == path_gates[i][j][0]:
                    start = path_gates[i][j - 1]
                    while j < len(path_gates[i]) - 1 and path_gates[i][j - 1][0] == path_gates[i][j][0] and \
                                   path_gates[i][j + 1][0] == path_gates[i][j][0]:
                        end = path_gates[i][j + 1]
                        j += 1
                    if j == len(path_gates[i]) - 1 and path_gates[i][j - 1][0] == path_gates[i][j][0] and \
                                   path_gates[i][j - 1][0] == path_gates[i][j - 2][0]:
                        end = path_gates[i][j]
                        j += 1
                    new_path_gates.append([start, end])
                    
                    
                elif j < len(path_gates[i]) - 1 and path_gates[i][j - 1][1] == path_gates[i][j][1] and \
                                   path_gates[i][j + 1][1] == path_gates[i][j][1]:
                    start = path_gates[i][j - 1]
                    while j < len(path_gates[i]) - 1 and path_gates[i][j - 1][1] == path_gates[i][j][1] and \
                                   path_gates[i][j + 1][1] == path_gates[i][j][1]:
                        end = path_gates[i][j + 1]
                        j += 1
                    if j == len(path_gates[i]) - 1 and path_gates[i][j - 1][1] == path_gates[i][j][1] and \
                                   path_gates[i][j - 1][1] == path_gates[i][j - 2][1]:
                        end = path_gates[i][j]
                        j += 1
                    new_path_gates.append([start, end])

                else:
                    start = path_gates[i][j - 1]
                    end = path_gates[i][j]
                    new_path_gates.append([start, end])

                if j == len(path_gates[i]) - 1 and not ((path_gates[i][j - 1][0] == path_gates[i][j][0] and \
                                path_gates[i][j - 1][0] == path_gates[i][j - 2][0]) or (path_gates[i][j - 1][1] \
                                == path_gates[i][j][1] and path_gates[i][j - 1][1] == path_gates[i][j - 2][1])):
                    new_path_gates.append([path_gates[i][j - 1], path_gates[i][j]])
                j += 1

        twice = []
        for i in range(len(new_path_gates)):
            for j in range(i + 1, len(new_path_gates)):
                if new_path_gates[j] == new_path_gates[i]:
                    twice.append(new_path_gates[i])
                    
        for each_element in twice:
            new_path_gates.remove(each_element)
                                   
        horizontal_0 = []
        horizontal = []
        vertical = []
        for each_element in new_path_gates:
            if each_element[0][0] == each_element[1][0]:
                horizontal_0.append(each_element)
            else:
                vertical.append([[each_element[0][1], each_element[0][0]], [each_element[1][1], each_element[1][0]]])
                        
        horizontal_0 = sorted(horizontal_0)
        vertical = sorted(vertical)
        
        for each_element in horizontal_0:
            horizontal.append([[each_element[0][1], each_element[0][0]], [each_element[1][1], each_element[1][0]]])
            
        out_h = []
        out_v = []
        for each_element in horizontal:
            if each_element[0][0] > each_element[1][0]:
                out_h.append([each_element[1], each_element[0]])
            else:
                out_h.append(each_element)

        for each_element in vertical:
            if each_element[0][1] > each_element[1][1]:
                out_v.append([each_element[1], each_element[0]])
            else:
                out_v.append(each_element)
            
    
        new_file.write('% Entry-exit paths without intersections\n')
        for i in range(len(out_h)):
            new_file.write(f'    \\draw[dashed, yellow] ({out_h[i][0][0]},{out_h[i][0][1]}) -- ({out_h[i][1][0]},{out_h[i][1][1]});\n')
        for i in range(len(out_v)):
            new_file.write(f'    \\draw[dashed, yellow] ({out_v[i][0][0]},{out_v[i][0][1]}) -- ({out_v[i][1][0]},{out_v[i][1][1]});\n')
        new_file.write('\\end{tikzpicture}\n')
        new_file.write('\\end{center}\n')
        new_file.write('\\vspace*{\\fill}\n')
        new_file.write('\n')
        new_file.write('\\end{document}\n')
        
        new_file.close()
'''       
maze1 = Maze('incorrect_input_1.txt')
maze2 = Maze('incorrect_input_2.txt')
maze3 = Maze('not_a_maze_1.txt')
maze4 = Maze('not_a_maze_2.txt')
'''
maze = Maze('new_maze.txt')
maze.display()
maze.analyse()
