
'''
Given strictly positive integers N and D, outputs N / D in the form
                 1 / d_1 + ... + 1 / d_k
if N < D, and in the form
                 p + 1 / d_1 + ... + 1 /d_k
if N >= D,
- for one function, applying Fibonacci's method (which yields a unique decomposition),
- for another function, determining all decompositions of minimal length (which might yield
  many decompositions).
'''


from math import gcd


# Possibly define other functions
def solve(N, D, results):
    if N > D:
        results.append(1)
        return solve(N - D, D, results)
    if not gcd(N, D) == 1:
        return solve(N // gcd(N, D), D // gcd(N, D), results)
    if N == 1:
        results.append(D)
        return
    else:
        d = D // N + 1
        results.append(d)
        return solve(N * d - D, D * d, results)

def fibonacci_decomposition(N, D):
    # Replace pass above with your code
    results = []
    solve(N, D, results)
    tmp = 0
    for d in results:
        if d == 1:
            tmp += 1
    for i in range(tmp):
        results.remove(1)
    if tmp > 0:
        results.append(tmp)

    output = str(N) + '/' + str(D) + ' = '
    if tmp > 0:
        output += str(tmp) + ' + '
        for i in range(len(results) - 1):
            output += '1/' + str(results[i]) + ' + '
    else:
        for i in range(len(results)):
            output += '1/' + str(results[i]) + ' + '
        
    output = output[:-3]
    print(output)
                     
def reduce(numerator, denominator):
    the_gcd = gcd(numerator, denominator)
    return numerator // the_gcd, denominator // the_gcd

def subtract(numerator, denominator, unit_denominator):
    '''
    Returns the reduced form of (numerator / denominator) - (1 / unit_denominator)
    '''
    numerator = numerator * unit_denominator - denominator
    denominator *= unit_denominator
    return reduce(numerator, denominator)

def shortest_length_decompositions(N, D):
    # Replace pass above with your code
    numerator, denominator = reduce(N, D)
    numerator %= denominator
    if not numerator:
        print(f'{N}/{D} = {N // D}')
        return
    length = 1
    while True:
        length += 1
        decompositions = fixed_length_decompositions(length, numerator, denominator, 2)
        if decompositions:
            for decomposition in decompositions:
                print(f'{N}/{D} = ', end = '')
                if N > D:
                    print(f'{N // D} + ', end = '')
                print(' + '.join(f'1/{unit_denominator}' for unit_denominator in decomposition))
            return

def fixed_length_decompositions(length, N, D, minimum):
    '''
    Returns the list of all lists of the form [d_1, d_2, ..., d_length] such that:
    - N / D = 1/d_1 + 1/d_2 + ... + 1/d_length;
    - minimum >= d_1 > d_2 > ... > d_length.
    '''
    if length == 1:
        if N == 1:
            return [[D]]
        return
    decompositions = []
    # Since we want N / D to be a sum of length many distinct terms,
    # the largest one being 1 / unit_denominator,
    # 1 / unit_denominator * length should be greater than N / D,
    # which is equivalent to unit_denominator < D * length / N,
    # which, since N and D are relatively prime, is equivalent to:
    #   - unit_denominator < D * length // N if N does not divide length;
    #   - unit_denominator < (D * length // N) + 1 if N divides length.   
    upper_bound = D * length // N
    if length % N:
        upper_bound += 1
    # 1 / unit_denominator should be smaller than N / D,
    # which is equivalent to unit_denominator > D / N,
    # which is equivalent to unit_denominator > D // N.   
    for unit_denominator in range(max(D // N + 1, minimum), upper_bound):
        numerator, denominator = subtract(N, D, unit_denominator)
        further_decompositions = fixed_length_decompositions(length - 1, numerator, denominator,
                                                                               unit_denominator + 1
                                                            )
        if further_decompositions:
            for decomposition in further_decompositions:
                decompositions.append([unit_denominator] + decomposition)
    return decompositions

                     
