# Prompts the user for an integer N and finds all perfect numbers up to N.
# Quadratic complexity, can deal with small values only.


import sys

# Insert your code here
perfect_number = []


try:
    N = int(input('Input an integer: '))
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

for number in range(2, N + 1):
    # Replace pass above with your code to check whether i is perfect,
    # and print out that it is in case it is.
    # 1 divides i, so counts for one divisor.
    # It is enough to look at 2, ..., i // 2 as other potential divisors.
    sum_div = 0
    for j in range(1, number // 2):
        if number % j == 0:
            sum_div += j
            # print(f'{j} of {number}')
    if sum_div == number:
        perfect_number.append(number)

for i in range(len(perfect_number)):
    print(f'{perfect_number[i]} is a perfect number.')
