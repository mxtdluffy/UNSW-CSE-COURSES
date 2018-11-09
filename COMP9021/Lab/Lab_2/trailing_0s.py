# Prompts the user to input an integer N at least equal to 10 and computes N!
# in three different ways.


import sys
from math import factorial

# Insert your code here
def first_computation(x):
    cnt = 0
    while x % 10 == 0:
        cnt += 1
        x = x // 10
    return cnt
    

def second_computation(x):
    cnt = 0
    while x[-1] == '0' and len(x) >= 1:
        cnt += 1
        x = x[:-1]
    return cnt
    
   

def third_computation(x):
    cnt = 0
    while x // 5:
        cnt = cnt + x // 5
        x = x // 5
    return cnt
    

try:
    the_input = int(input('Input a nonnegative integer: '))
    if the_input < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

the_input_factorial = factorial(the_input)
print(f'Computing the number of trailing 0s in {the_input}! by dividing by 10 for long enough:',
      first_computation(the_input_factorial))
print(f'Computing the number of trailing 0s in {the_input}! by converting it into a string:',
      second_computation(str(the_input_factorial)))
print(f'Computing the number of trailing 0s in {the_input}! the smart way:',
      third_computation(the_input))
