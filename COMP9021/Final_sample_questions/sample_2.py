def solve(value, result, banknote_values):
    if not value:
        return
    for i in range(7):
        if value >= banknote_values[6 - i]:
            result[6 - i] += 1
            value -= banknote_values[6 - i]
            return solve(value, result, banknote_values)
        
        
    
def f(N):
    '''
    >>> f(20)
    Here are your banknotes:
    $20: 1
    >>> f(40)
    Here are your banknotes:
    $20: 2
    >>> f(42)
    Here are your banknotes:
    $2: 1
    $20: 2
    >>> f(43)
    Here are your banknotes:
    $1: 1
    $2: 1
    $20: 2
    >>> f(45)
    Here are your banknotes:
    $5: 1
    $20: 2
    >>> f(2537)
    Here are your banknotes:
    $2: 1
    $5: 1
    $10: 1
    $20: 1
    $100: 25
    '''
    banknote_values = [1, 2, 5, 10, 20, 50, 100]
    # Insert your code here
    result = [0, 0, 0, 0, 0, 0, 0]
    solve(N, result, banknote_values)
    print('Here are your banknotes:')
    for i in range(7):
        if result[i]:
            print(f'${banknote_values[i]}: {result[i]}')
                        
'''
if __name__ == '__main__':
    import doctest
    doctest.testmod()
'''
f(20)
f(40)
f(42)
f(43)
f(45)
f(2537)

