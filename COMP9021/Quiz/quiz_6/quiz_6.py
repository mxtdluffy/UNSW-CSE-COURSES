# Randomly fills an array of size 10x10 True and False, displayed as 1 and 0,
# and outputs the number chess knights needed to jump from 1s to 1s
# and visit all 1s (they can jump back to locations previously visited).
#
# Written by Jingyun Shen and Eric Martin for COMP9021


from random import seed, randrange
import sys


dim = 10

def display_grid():
    for i in range(dim):
        print('     ', end = '')
        print(' '.join(grid[i][j] and '1' or '0' for j in range(dim)))
    print()

def find_knight_class(point_list, point):
    pointx = point[0]
    pointy = point[1]
    point_list.remove(point)
    next_steps = [[pointx - 1, pointy - 2], [pointx - 2, pointy - 1], \
                  [pointx - 2, pointy + 1], [pointx - 1, pointy + 2], \
                  [pointx + 1, pointy - 2], [pointx + 2, pointy - 1], \
                  [pointx + 2, pointy + 1], [pointx + 1, pointy + 2]]
    for next_point in next_steps:
        if next_point in point_list:
            find_knight_class(point_list, next_point)
        
    return point_list
    
def explore_board():
    point_list = []
    for i in range(dim):
        for j in range(dim):
            if grid[i][j]:
                point_list.append([j, i])

    if len(point_list) == 0:
        return 0
    else:
        nb_of_knights = 0
        while not len(point_list) == 0:
            point_list = find_knight_class(point_list, point_list[0])
            nb_of_knights += 1
        return nb_of_knights
    

try:
    for_seed, n = (int(i) for i in input('Enter two integers: ').split())
    if not n:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
if n > 0:
    grid = [[randrange(n) > 0 for _ in range(dim)] for _ in range(dim)]
else:
    grid = [[randrange(-n) == 0 for _ in range(dim)] for _ in range(dim)]    
print('Here is the grid that has been generated:')
display_grid()
nb_of_knights = explore_board()

if not nb_of_knights:
    print('No chess knight has explored this board.')
elif nb_of_knights == 1:
    print(f'At least 1 chess knight has explored this board.')
else:
    print(f'At least {nb_of_knights} chess knights have explored this board')

