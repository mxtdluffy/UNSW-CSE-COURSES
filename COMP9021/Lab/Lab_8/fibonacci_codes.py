'''
Every strictly positive integer N can be uniquely coded as a string sigma
of 0's and 1's ending with 1, so of the form b_2b_3...b_k with k >= 2 and b_k = 1,
such that N is the sum of all F_i's, 2 <= i <= k, with b_i = 1.

Moreover:
- there are no two successive occurrences of 1 in sigma;
- F_k is the largest Fibonacci number that fits in N, and
  if j is the largest integer in {2,...,k-1} such that b_j = 1
  then F_j is the largest Fibonacci number that fits in N - F_k, and
  if i is the largest integer in {2,...,j-1} such that b_i = 1
  then F_i is the largest Fibonacci number that fits in  N - F_k - F_j...

Also, every string of 0's and 1's ending in 1 and having no two
successive occurrences of 1's is a code of a strictly positive integer
according to this coding scheme. For instance:
- There is only one string of 0's and 1's of length 1 ending in 1 and
  having no two successive occurrences of 1's; it is 1, and it codes 1.
- There is only one string of 0's and 1's of length 2 ending in 1 and
  having no two successive occurrences of 1's; it is 01, and it codes 2.
- The strings of 0's and 1's of length 3 ending in 1 and having no two successive occurrences
  of 1's are 001 and 101 and they code 3 and 4, respectively.
- The strings of 0's and 1's of length 4 ending in 1 and having no two successive occurrences
  of 1's are 0001, 1001 and 0101 and they code 5, 6 and 7, respectively.
- The strings of 0's and 1's of length 5 ending in 1 and having no two successive occurrences
  of 1's are 00001, 10001, 01001, 00101 and 10101 and they code 8, 9, 10, 11 and 12, respectively.
- ...

The Fibonacci code of N adds 1 at the end of sigma; the resulting string then ends in two 1's,
therefore marking the end of the code, and allowing one to let one string code a finite sequence
of strictly positive integers. For instance, 00101100111011 codes (11,3,4).
'''

def fib(nb):
    if nb == 0:
        return [0]
    if nb == 1:
        return [0, 1]
    if nb > 1:
        result = [0, 1]
        for i in range(nb - 1):
            result.append(result[-1] + result[-2])
        return result

def encode(n):
    '''
    Retuns the Fibonacci code of n, meant to be a strictly positive integer.
    '''
    # Replace pass above with your code
    if n <= 0:
        return '0'

    nb = 1
    while True:
        fib_array = fib(nb)
        if fib_array[-1] > n:
            break
        nb += 1
        
    fib_array = fib_array[2: -1] # fib_array = [F2, F3, ..., Fk]
    nb -= 2 # nb = len(fib_array)
    visited = [False] * nb
    left_n = n

    cur = 0
    while cur < nb:
        if cur > 0 and visited[nb - cur]:
            cur += 1
            continue
        if left_n >= fib_array[nb - cur - 1]:
            visited[nb - cur - 1] = True
            left_n -= fib_array[nb - cur - 1]
        cur += 1

    output = ''
    for i in range(len(visited)):
        if visited[i]:
            output += '1'
        else:
            output += '0'
    output += '1'
    return output
    

def decode(code):
    '''
    The argument is meant to be a string of 0's and 1's.
    Returns 0 if the argument cannot be a Fibonacci code;
    otherwise returns the integer argument is the Fibonacci code of.
    '''
    # Replace pass above with your code
    code = code[:-1]
    if code == '':
        return 0
    if not code[-1] == '1':
        return 0
    for i in range(len(code) - 1):
        if code[i] == code[i + 1] == '1':
            return 0
    length = len(code) + 2
    fib_array = fib(length)
    fib_array = fib_array[2:]
    
    output = 0
    for i in range(len(code)):
        if code[i] == '1':
            output += fib_array[i]
    return output

print(encode(14), encode(12), encode(10), encode(1), encode(2))
print(decode('1'), decode('100011011'), decode('11'), decode('011'), decode('1000011'))

