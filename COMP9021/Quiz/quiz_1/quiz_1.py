# Written by Jingyun Shen and Eric Martin for COMP9021



import sys
from random import seed, randrange


try:
    arg_for_seed = int(input('Enter an integer: '))
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
x = randrange(10 ** 10)
sum_of_digits_in_x = 0
L = [randrange(10 ** 8) for _ in range(10)]
first_digit_greater_than_last = 0
same_first_and_last_digits = 0
last_digit_greater_than_first = 0
distinct_digits = [0] * 9
min_gap = 10
max_gap = -1
first_and_last = set()


# REPLACE THIS COMMENT WITH YOUR CODE

# The sum of all digits in x
def get_sum(x):
    str_x = str(x)
    sum_x = 0
    for i in range(len(str_x)):
        sum_x += int(str_x[i])
    return sum_x

# The first digit is greater than the last digit
def f_greater_l(L):
    cnt = 0
    for number in range(len(L)):
        str_n = str(L[number])
        if str_n[0] > str_n[len(str_n) - 1]:
            cnt += 1
    return cnt

# The first digit equals to the last digit
def f_equal_l(L):    
    cnt = 0
    for number in range(len(L)):
        str_n = str(L[number])
        if str_n[0] == str_n[len(str_n) - 1]:
            cnt += 1
    return cnt

# The first digit is smaller than the last digit
def f_smaller_l(L):    
    cnt = 0
    for number in range(len(L)):
        str_n = str(L[number])
        if str_n[0] < str_n[len(str_n) - 1]:
            cnt += 1
    return cnt

# The number of members of L - distinct digits
def find_distinct(number):
    n_store = [0] * 10
    str_n = str(number)
    cnt = 0
    for i in range(len(str_n)):
        n_store[int(str_n[i])] += 1
    for i in range(10):
        if n_store[i]:
            cnt += 1
    return cnt

def find_distinct_digit(L, distinct_digits):
    for i in range(len(L)):
        distinct = find_distinct(L[i])
        distinct_digits[distinct] += 1
    return distinct_digits

# The minimal gap (in absolute value) between first and last digits
def find_gap(number):
    str_n = str(number)
    gap = abs(int(str_n[0]) - int(str_n[-1])) 
    return gap

def find_min_gap(L):
    min_gap = 99999
    for i in range(len(L)):
        if find_gap(L[i]) < min_gap:
            min_gap = find_gap(L[i])
    return min_gap

# The maximal gap (in absolute value) between first and last digits
def find_max_gap(L):
    max_gap = 0
    for i in range(len(L)):
        if find_gap(L[i]) > max_gap:
            max_gap = find_gap(L[i])
    return max_gap

# The number of pairs (f, l) such that f and l are the first and
# last digits of members of L is maximal for (f, l)
def find_pairs(L):
    pair_list = []
    for i in range(len(L)):
        str_n = str(L[i])
        pair_list.append((int(str_n[0]), int(str_n[len(str_n) - 1])))
    return pair_list
    
def find_max_pairs(L):
    pair_list = find_pairs(L)
    distinct_pair_list = list(set(pair_list))
    distinct_list = [0] * len(distinct_pair_list)
    for i in range(len(distinct_pair_list)):
        cur_pair = distinct_pair_list[i]
        cnt = 0
        for j in range(len(pair_list)):
            if pair_list[j] == cur_pair:
                cnt += 1
        distinct_list[i] = cnt
    max_cnt = max(distinct_list)
    for i in range(len(distinct_list)):
        if distinct_list[i] == max_cnt:
            first_and_last.add(distinct_pair_list[i])
    return first_and_last

             

sum_of_digits_in_x = get_sum(x)
first_digit_greater_than_last = f_greater_l(L)
same_first_and_last_digits = f_equal_l(L)
last_digit_greater_than_first = f_smaller_l(L)
distinct_digits = find_distinct_digit(L, distinct_digits)
min_gap = find_min_gap(L)
max_gap = find_max_gap(L)
first_and_last = find_max_pairs(L)


print()
print('x is:', x)
print('L is:', L)
print()
print(f'The sum of all digits in x is equal to {sum_of_digits_in_x}.')
print()
print(f'There are {first_digit_greater_than_last}, {same_first_and_last_digits} '
      f'and {last_digit_greater_than_first} elements in L with a first digit that is\n'
      '  greater than the last digit, equal to the last digit,\n'
      '  and smaller than the last digit, respectively.'
     )
print()
for i in range(1, 9):
    if distinct_digits[i]:
        print(f'The number of members of L with {i} distinct digits is {distinct_digits[i]}.')
print()
print('The minimal gap (in absolute value) between first and last digits\n'
      f'  of a member of L is {min_gap}.'
     )
print('The maximal gap (in absolute value) between first and last digits\n'
      f'  of a member of L is {max_gap}.')
print()
print('The number of pairs (f, l) such that f and l are the first and last digits\n'
      f'of members of L is maximal for (f, l) one of {sorted(first_and_last)}.'
     )
        
