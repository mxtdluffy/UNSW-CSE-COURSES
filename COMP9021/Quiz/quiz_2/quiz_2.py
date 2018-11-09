# Written by Jingyun and Eric Martin for COMP9021



import sys
from random import seed, randint
from math import gcd


try:
    arg_for_seed, length, max_value = input('Enter three strictly positive integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, length, max_value = int(arg_for_seed), int(length), int(max_value)
    if arg_for_seed < 1 or length < 1 or max_value < 1:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
L = [randint(1, max_value) for _ in range(length)]
print('Here is L:')
print(L)
print()

size_of_simplest_fraction = None
min_complex_fractions = []
size_of_most_complex_fraction = None
most_complex_fractions = []
multiplicity_of_largest_prime_factor = 0
largest_prime_factors = []

# REPLACE THIS COMMENT WITH YOUR CODE
sorted_L = sorted(L)

# Create the simplest_fractions[]
simplest_fractions = []
for i in range(length):
    for j in range(i, length):
        GCD = gcd(sorted_L[i], sorted_L[j])
        simplest_fractions.append((sorted_L[i] // GCD, sorted_L[j] // GCD))
simplest_fractions = list(set(simplest_fractions))

# Record the complexity of the simplest fractions
complexity = []
for i in range(len(simplest_fractions)):
    each_len = len(str(simplest_fractions[i][0])) + \
               len(str(simplest_fractions[i][1]))
    complexity.append(each_len)

# Find the minimal complexity in complexity[] and simplest_fractions[]
size_of_simplest_fraction = min(complexity)
unsorted_simplest_fractions = []
for i in range(len(simplest_fractions)):
    each_len = len(str(simplest_fractions[i][0])) + \
               len(str(simplest_fractions[i][1]))
    if each_len == size_of_simplest_fraction:
        unsorted_simplest_fractions.append(simplest_fractions[i])
        
sort_simplest_fractions = []
for i in range(len(unsorted_simplest_fractions)):
    sort_simplest_fractions.append((unsorted_simplest_fractions[i][0] / unsorted_simplest_fractions[i][1], i))
sort_simplest_fractions = sorted(sort_simplest_fractions)

for i in range(len(sort_simplest_fractions)):
    index = sort_simplest_fractions[i][1]
    min_complex_fractions.append((unsorted_simplest_fractions[index]))

# Find the maximal complexity in complexity[] and simplest_fractions[]
size_of_most_complex_fraction = max(complexity)
unsorted_most_complex = []
for i in range(len(simplest_fractions)):
    each_len = len(str(simplest_fractions[i][0])) + \
               len(str(simplest_fractions[i][1]))
    if each_len == size_of_most_complex_fraction:
        unsorted_most_complex.append(simplest_fractions[i])
        
sort_most_complex = []
for i in range(len(unsorted_most_complex)):
    sort_most_complex.append((unsorted_most_complex[i][0] / unsorted_most_complex[i][1], i))
sort_most_complex = sorted(sort_most_complex, reverse = True)

for i in range(len(sort_most_complex)):
    index = sort_most_complex[i][1]
    most_complex_fractions.append((unsorted_most_complex[index]))

# Find the highest multiplicity of prime factors of the latter's denominators

denominators = []
for i in range(len(most_complex_fractions)):
    denominators.append(most_complex_fractions[i][1])
denominators = list(set(denominators))

def find_prime_factors(num):
    n = num 
    f = []  
    for j in range(int(num / 2) + 1):  
        for i in range(2, n + 1):
            t = n % i  
            if t == 0:  
                f.append(i)  
                n = n // i  
                break  
    f.append(n)  
    f.sort()  
    f.remove(1)

    result = []
    i = 0
    j = 1
    while i < len(f):
        cnt = 1
        while j < len(f): 
            if f[i] == f[j]:
                cnt += 1
                j += 1
            else:
                # print("f[i]", f[i])
                # print("i:",i)
                # print("j:",j)
                result.append((f[i], j - i))
                i = j
                continue
        result.append((f[i], j - i))
        break
    return result

def _1_0(s):
    return s[1], s[0]

if denominators == [1]:
    multiplicity_of_largest_prime_factor = 0
    largest_prime_factors = []
else:
    prime_factors_denominators = []
    max_multiplicity = []
    for i in range(len(denominators)):
        each_prime_factors = sorted(find_prime_factors(denominators[i]), key = _1_0, reverse = True)
        max_multiplicity.append(each_prime_factors[0][1])
        prime_factors_denominators.append(each_prime_factors)
    multiplicity_of_largest_prime_factor = max(max_multiplicity)

    for i in range(len(prime_factors_denominators)):
        for j in range(len(prime_factors_denominators[i])):
            if multiplicity_of_largest_prime_factor == prime_factors_denominators[i][j][1]:
                largest_prime_factors.append(prime_factors_denominators[i][j][0])           
    largest_prime_factors = list(set(largest_prime_factors))
    largest_prime_factors = sorted(largest_prime_factors)

    
print('The size of the simplest fraction <= 1 built from members of L is:',
      size_of_simplest_fraction
     )
print('From smallest to largest, those simplest fractions are:')
print('\n'.join(f'    {x}/{y}' for (x, y) in min_complex_fractions))
print('The size of the most complex fraction <= 1 built from members of L is:',
      size_of_most_complex_fraction
     )
print('From largest to smallest, those most complex fractions are:')
print('\n'.join(f'    {x}/{y}' for (x, y) in most_complex_fractions))
print("The highest multiplicity of prime factors of the latter's denominators is:",
      multiplicity_of_largest_prime_factor
     )
print('These prime factors of highest multiplicity are, from smallest to largest:')
print('   ', largest_prime_factors)
        
        
