# Given a positive integer n, a magic square of order n is a matrix of size n x n
# that stores all numbers from 1 up to n^2 and such that the sum of the n rows,
# the sum of the n columns, and the sum of the two diagonals is constant,
# hence equal to n(n^2+1)/2.


def is_magic_square(square):
    result = True
    n = len(square[0])
    for i in range(n):
        total1 = 0
        for j in range(n):
            total1 += square[i][j]
        if not total1 == n * (n ** 2 + 1) // 2:
            result = False
            return result

    for i in range(n):
        total2 = 0
        for j in range(n):
            total2 += square[j][i]
        if not total2 == n * (n ** 2 + 1) // 2:
            result = False
            return result
        
    total3 = 0
    for i in range(n):
        total3 += square[i][i]
    if not total3 == n * (n ** 2 + 1) // 2:
        result = False
        return result

    total4 = 0
    for i in range(n):
        total4 += square[i][n - i - 1]
    if not total4 == n * (n ** 2 + 1) // 2:
        result = False
        return result

    return result

        
def print_square(square):
    for each_list in square:
        tmp = ''
        for each_item in each_list:
            tmp += str(each_item) + ' '
        tmp = tmp[:-1]
        print(tmp)

''' 
print_square([[2,7,6], [9,5,1], [4,3,8]])
print(is_magic_square([[2,7,6], [9,5,1], [4,3,8]]))
print_square([[2,7,6], [1,5,9], [4,3,8]])
print(is_magic_square([[2,7,6], [1,5,9], [4,3,8]]))
'''
