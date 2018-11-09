import os.path
import sys

from collections import defaultdict

try:
    open_file = input("Please enter the name of the file you want to get data from: ")
    f = open(open_file, 'r')
except FileNotFoundError:
    print("Sorry, there is no such file.\n")
    sys.exit()

cable_car = []
with open(open_file) as cable_car_file:
    for line in cable_car_file:
        each_line = list(filter(None, line.split(' ')))
        cable_car += each_line
f.close()

try:
    for i in range(len(cable_car)):
        if cable_car[i].endswith('\n'):
            cable_car[i] = cable_car[i][:-1]
            if not cable_car[i] == '':
                cable_car[i] = int(cable_car[i])
                if cable_car[i] <= 0:
                    raise ValueError
        else:
            cable_car[i] = int(cable_car[i])
            if cable_car[i] <= 0:
                raise ValueError

    while '' in cable_car:
        cable_car.remove('')
        
    if len(cable_car) < 2:
        raise ValueError
    for i in range(len(cable_car) - 1):
        if not cable_car[i] < cable_car[i + 1]:
            raise ValueError       
except ValueError:
    print("Sorry, input file does not store valid data.")
    sys.exit()

# Store all the intervals between two consecutive numbers
store_interval = []
for i in range(len(cable_car) - 1):
    store_interval.append(cable_car[i + 1] - cable_car[i])

# Judge whether the current ride is perfect
def judge_perfect(cable_car):
    interval = cable_car[1] - cable_car[0]
    perfect = True
    for i in range(len(cable_car) - 1):
        if not cable_car[i + 1] - cable_car[i] == interval:
            perfect = False
            break
    return perfect

# Find the longest ride by finding the longest consecutive equal number
def find_longest_ride(store_interval):
    store_ride = []
    i = 0
    while i < len(store_interval):
        cur_interval = store_interval[i]
        cnt = 1
        i += 1
        while i < len(store_interval):
            if cur_interval == store_interval[i]:
                cnt += 1
                i += 1
                if i == len(store_interval):
                    store_ride.append(cnt)
            else:
                store_ride.append(cnt)
                break
        
    longest_ride = max(store_ride)
    return longest_ride

# Find the minimal number of pillars to remove to build a perfect ride
def find_min_remove(cable_car):
    min_remove = 0
    n = len(cable_car)
    dp = [([2] * n) for i in range(n)]
    longest = 1

    j = n - 2
    while j >= 0:
        i = j - 1
        k = j + 1
        while i >= 0 and k < n:
            if cable_car[i] + cable_car[k] == cable_car[j] * 2:
                dp[i][j] = dp[j][k] + 1
                longest = max(longest, dp[i][j])
                i -= 1
                k += 1
            elif cable_car[i] + cable_car[k] > cable_car[j] * 2:
                i -= 1
            else:
                k += 1
        j -= 1

    min_remove = n - longest

    return min_remove
    
perfect = judge_perfect(cable_car)
longest_ride = find_longest_ride(store_interval)

print("cable_car:",cable_car)

if perfect:
    print("The ride is perfect!")
    min_remove = 0
    print("The longest good ride has a length of:", longest_ride)
    print("The minimal number of pillars to remove to build a perfect ride from the rest is:", min_remove)

else:
    print("The ride could be better...")
    min_remove = find_min_remove(cable_car)
    print("The longest good ride has a length of:", longest_ride)
    print("The minimal number of pillars to remove to build a perfect ride from the rest is:", min_remove)


