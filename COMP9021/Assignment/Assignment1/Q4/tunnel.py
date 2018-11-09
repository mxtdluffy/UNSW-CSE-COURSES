import os.path
import sys
from collections import deque

try:
    open_file = input("Please enter the name of the file you want to get data from: ")
    f = open(open_file, 'r')
except FileNotFoundError:
    print("Sorry, there is no such file.\n")
    sys.exit()

tunnel_init = []
with open(open_file) as tunnel_file:
    for line in tunnel_file:
        each_line = list(filter(None, line.split(' ')))
        tunnel_init += each_line
f.close()

tunnel = [[]]
idx = 0
try:
    for i in range(len(tunnel_init)):
        if tunnel_init[i].endswith('\n'):
            tunnel_init[i] = tunnel_init[i][:-1]
            if not tunnel_init[i] == '':
                tunnel[idx].append(int(tunnel_init[i]))
                tunnel.append([])
                idx += 1
            else:
                tunnel.append([])
                idx += 1
        else:
            tunnel[idx].append(int(tunnel_init[i]))
            
    while [] in tunnel:
        tunnel.remove([])
        
    if not (len(tunnel) == 2 and len(tunnel[0]) == len(tunnel[1]) \
            and len(tunnel[0]) >= 2):
        raise ValueError

    for i in range(len(tunnel[0])):
        if not tunnel[0][i] > tunnel[1][i]:
            raise ValueError   
    
except ValueError:
    print("Sorry, input file does not store valid data.")

# Find the longest tunnel from the west
def find_west_tunnel(tunnel):
    west_tunnel = 0
    for i in range(len(tunnel[0])):
        height = min(tunnel[0][:(i + 1)])
        if height <= max(tunnel[1][:(i + 1)]):
            break
        else:
            west_tunnel += 1
        
    return west_tunnel

# Find the longest tunnel inside the tunnel
# First, find all the tunnels (up-based & down-based).
# Then, find the longest one.

def find_tunnel(rcd):
    tmp = []
    cur_length = 0
    
    for i in range(len(rcd)):
        if rcd[i]:
            cur_length += 1          
        else:
            tmp.append(cur_length)
            cur_length = 0
    tmp.append(cur_length)
            
    return max(tmp)

def find_inside_tunnel(tunnel):

    max_height = max(tunnel[0])
    min_height = min(tunnel[1])

    # Create detect height
    detect_height = []
    cur_height = max_height - 0.5
    while cur_height > min_height:
        detect_height.append(cur_height)
        cur_height -= 1

    all_tunnels = []
    for test_height in detect_height:
        rcd = [None] * len(tunnel[0])
        
        for i in range(len(tunnel[0])):
            if test_height < tunnel[0][i] and test_height > tunnel[1][i]:
                rcd[i] = True
            else:
                rcd[i] = False
            # print(f"{test_height}: {rcd[i]}")
                
        all_tunnels.append(find_tunnel(rcd))
        # print(f"max_length: {find_tunnel(rcd)}")

    longest_inside_tunnel = max(all_tunnels)
    
    return longest_inside_tunnel

west_tunnel = find_west_tunnel(tunnel)
longest_inside_tunnel = find_inside_tunnel(tunnel)
print(f"From the west, one can see into the tunnel over a distance of {west_tunnel}.")
print(f"Inside the tunnel, one can see into the tunnel over a maximum distance of {longest_inside_tunnel}.")
