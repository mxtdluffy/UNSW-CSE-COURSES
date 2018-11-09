# Randomly fills a grid of size 7 x 7 with NE, SE, SW, NW,
# meant to represent North-East, South-East, North-West, South-West,
# respectively, and starting from the cell in the middle of the grid,
# determines, for each of the 4 corners of the grid, the preferred path amongst
# the shortest paths that reach that corner, if any. At a given cell, it is possible to move
# according to any of the 3 directions indicated by the value of the cell;
# e.g., from a cell storing NE, it is possible to move North-East, East, or North.
# At any given point, one prefers to move diagonally, then horizontally,
# and vertically as a last resort.
#
# Written by Jingyun SHen and Eric Martin for COMP9021


import sys
from random import seed, choice
from queue_adt import *


def display_grid():
    for row in grid:
        print('    ', *row)

class GeneralTree:
    def __init__(self, value1 = None, value2 = None):
        self.value1 = value1
        self.value2 = value2
        self.parent = None
        self.children = []

    def set_children(self, children):
        if self.value1 is None:
            return
        self.children = children
        
    def set_parent(self, par_node):
        self.parent = par_node
        
    def get_value1(self):
        return self.value1

    def get_value2(self):
        return self.value2

    def get_parent(self):
        return self.parent

def create_tree(each_node):
    global detect_grid
    children = []
    possible_children = []
    mark = [False, False, False]
    temp = each_node.get_value2()
    detect_grid[temp[0]][temp[1]] = True
    if each_node.get_value1() == 'NE':
        if temp[0] > 0:
            possible_children.append([temp[0] - 1, temp[1]])
        if temp[1] < dim - 1:
            possible_children.append([temp[0], temp[1] + 1])
        if temp[0] > 0 and temp[1] < dim - 1:
            possible_children.append([temp[0] - 1, temp[1] + 1])       
        
    elif each_node.get_value1() == 'SE':
        if temp[0] < dim - 1:
            possible_children.append([temp[0] + 1, temp[1]])
        if temp[1] < dim - 1:
            possible_children.append([temp[0], temp[1] + 1])
        if temp[0] < dim - 1 and temp[1] < dim - 1:
            possible_children.append([temp[0] + 1, temp[1] + 1])

    elif each_node.get_value1() == 'SW':
        if temp[0] < dim - 1:
            possible_children.append([temp[0] + 1, temp[1]])
        if temp[1] > 0:
            possible_children.append([temp[0], temp[1] - 1])
        if temp[0] < dim - 1 and temp[1] > 0:
            possible_children.append([temp[0] + 1, temp[1] - 1])
            
    elif each_node.get_value1() == 'NW':
        if temp[0] > 0:
            possible_children.append([temp[0] - 1, temp[1]])
        if temp[1] > 0:
            possible_children.append([temp[0], temp[1] - 1])
        if temp[0] > 0 and temp[1] > 0:
            possible_children.append([temp[0] - 1, temp[1] - 1])

    for i in range(len(possible_children)):
        if not detect_grid[possible_children[i][0]][possible_children[i][1]]:
            children.append(tree_grid[possible_children[i][0]][possible_children[i][1]])
            tree_grid[possible_children[i][0]][possible_children[i][1]].set_parent(temp)
            detect_grid[possible_children[i][0]][possible_children[i][1]] = True
            mark[i] = True
            
    if mark[0] == mark[1] and mark[1] == mark[2] and mark[2] == False:
    
        return

    output = []
    for i in range(len(children)):
        output.append(children[i].get_value2())
    print(f'{each_node.get_value2()}\'s children are: {output}')

        
    each_node.set_children(children)
    
    for i in range(3):
        if mark[i] and (not (possible_children[i] == [0, 0]
                        or possible_children[i] == [dim - 1, 0]
                        or possible_children[i] == [0, dim - 1]
                        or possible_children[i] == [dim - 1, dim - 1])):
            create_tree(tree_grid[possible_children[i][0]][possible_children[i][1]])
        if mark[i] and possible_children[i] == [0, 0]:
            if_paths_exist[0] = True           
        elif mark[i] and possible_children[i] == [dim - 1, 0]:
            if_paths_exist[3] = True
        elif mark[i] and possible_children[i] == [dim - 1, dim - 1]:
            if_paths_exist[2] = True
        elif mark[i] and possible_children[i] == [0, dim - 1]:
            if_paths_exist[1] = True
        
def create_a_tree():
    create_tree(tree_grid[size][size])

def path_queue(a_corner):
    tmp_queue.enqueue(a_corner)
    if tree_grid[a_corner[0]][a_corner[1]].get_parent() == None:
        return
    else:
        cur_parent = tree_grid[a_corner[0]][a_corner[1]].get_parent()
        path_queue(cur_parent)

def find_path(a_corner):
    tmp_queue = Queue()
    
    def path_queue(a_corner):
        tmp_queue.enqueue(a_corner)
        if tree_grid[a_corner[0]][a_corner[1]].get_parent() == None:
            return
        else:
            cur_parent = tree_grid[a_corner[0]][a_corner[1]].get_parent()
            path_queue(cur_parent)

    path_queue(a_corner)
    store_path = []
    while not tmp_queue.is_empty():
        cur_node = tmp_queue.dequeue()
        store_path.append((cur_node[1], cur_node[0]))
    store_path.reverse() 
    return store_path
    
def preferred_paths_to_corners():
    paths = dict()
    for i in range(4):
        if if_paths_exist[i]:
            cur_path = find_path([corners[i][1], corners[i][0]])
            paths[corners[i]] = cur_path
    return paths

try:
    seed_arg = int(input('Enter an integer: '))
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
    
seed(seed_arg)
size = 3
dim = 2 * size + 1
detect_grid = [[False for _ in range(dim)] for _ in range(dim)]

grid = [[0] * dim for _ in range(dim)]
directions = 'NE', 'SE', 'SW', 'NW'

grid = [[choice(directions) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()

tree_grid = [[None for _ in range(dim)] for _ in range(dim)]
for i in range(dim):
    for j in range(dim):
        tree_grid[i][j] = GeneralTree(grid[i][j], [i, j])


corners = (0, 0), (dim - 1, 0), (dim - 1, dim - 1), (0, dim - 1)
if_paths_exist = [False] * 4
create_a_tree()
paths = preferred_paths_to_corners()

if not paths:
    print('There is no path to any corner')
    sys.exit()
for corner in corners:
    if corner not in paths:
        print(f'There is no path to {corner}')
    else:
        print(f'The preferred path to {corner} is:')
        print('  ', paths[corner])
