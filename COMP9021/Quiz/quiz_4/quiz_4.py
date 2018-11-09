# Randomly fills an array of size 10x10 with True and False, and outputs the number of blocks
# in the largest block construction, determined by rows of True's that can be stacked
# on top of each other. 
#
# Written by Jingyun Shen and Eric Martin for COMP9021


from random import seed, randrange
import sys


dim = 10


def display_grid():
    for i in range(dim):
        print('     ', end = '')
        print(' '.join(f'{int(e)}' for e in grid[i]))
    print()


def size_of_largest_construction():
    all_construction = []
    for row in range(dim):
        for column1 in range(dim):
            for column2 in range(column1, dim):
                con_size = construction_size(row, column1, column2)
                all_construction.append(con_size)
    return max(all_construction)

# If j1 <= j2 and the grid has a 1 at the intersection of row i and column j
# for all j in {j1, ..., j2}, then returns the number of blocks in the construction
# built over this line of blocks.
def construction_size(i, j1, j2):
    cnt = 0
    for column in range(j1, j2 + 1):
        if not grid[i][column]:
            break
        for row in range(i + 1):
            if grid[i - row][column]:
                cnt += 1
            else:
                break
    return cnt

            
try:
    for_seed, n = input('Enter two integers, the second one being strictly positive: ').split()
    for_seed = int(for_seed)
    n = int(n)
    if n <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[bool(randrange(n)) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()
size = size_of_largest_construction()
if not size:
    print(f'The largest block construction has no block.')  
elif size == 1:
    print(f'The largest block construction has 1 block.')  
else:
    print(f'The largest block construction has {size_of_largest_construction()} blocks.')  
