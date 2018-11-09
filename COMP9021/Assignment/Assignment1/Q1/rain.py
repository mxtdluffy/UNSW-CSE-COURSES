import sys

try:
    open_file = input("Which data file do you want to use? ")
    f = open(open_file, 'r')
except FileNotFoundError:
    print("Error!There is not such file in current directory.")
    sys.exit()

try:
    water = int(input("How many decilitres of water do you want to pour down? "))
except ValueError:
    print("Invalid input!")
    sys.exit()

height_of_land = []
with open(open_file) as land_file:
    for line in land_file:
        each_line = list(filter(None, line.split(' ')))
        height_of_land += each_line
f.close()

for i in range(len(height_of_land)):
    if height_of_land[i].endswith('\n'):
        height_of_land[i] = int(height_of_land[i][:-1])
    else:
        height_of_land[i] = int(height_of_land[i])
    
def find_height(height_of_land, water):
    cur = 1
    visited_cnt = []
    while True:
        cnt = height_of_land.count(cur)
        visited_cnt.append(cnt)
        if water - sum(visited_cnt) > 0:
            water -= sum(visited_cnt)
            cur += 1
        else:            
            height = cur + water / sum(visited_cnt)
            return height

height = find_height(height_of_land, water)
print(f'The water rises to {height:.2f} centimetres.\n')
