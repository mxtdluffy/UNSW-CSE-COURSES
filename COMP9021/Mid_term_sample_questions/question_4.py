import sys
from math import sqrt

def is_prime(number):
    result = True
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            result = False
            break
    return result

def f(n):
    '''
    Won't be tested for n greater than 10_000_000
    
    >>> f(3)
    The largest prime strictly smaller than 3 is 2.
    >>> f(10)
    The largest prime strictly smaller than 10 is 7.
    >>> f(20)
    The largest prime strictly smaller than 20 is 19.
    >>> f(210)
    The largest prime strictly smaller than 210 is 199.
    >>> f(1318)
    The largest prime strictly smaller than 1318 is 1307.
    '''
    if n <= 2:
        sys.exit()
    largest_prime_strictly_smaller_than_n = 0
    # Insert your code here
    cur = n - 1
    while cur >= 2:
        if is_prime(cur):
            break
        else:
            cur -= 1
    largest_prime_strictly_smaller_than_n = cur
    print(f'The largest prime strictly smaller than {n} is {largest_prime_strictly_smaller_than_n}.')

f(3)
f(10)
f(20)
f(210)
f(1318)

'''

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    '''
