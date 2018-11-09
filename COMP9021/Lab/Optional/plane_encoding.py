from math import sqrt


def encode(a, b):
    level = max(abs(a), abs(b)) * 2 + 1
    if not level == 1:
        start_row = ((level - 1) // 2 - 1) * (-1)
        start_column = (level - 1) // 2
    else:
        start_row = start_column = 0
        return 0
    
    row = start_row
    column = start_column
    number = (level - 2) ** 2
    
    if a == column and b == row:
        return number
    
    for i in range(1, level - 1):
        number += 1
        row += 1
        if a == column and b == row:
            return number
    for i in range(1, level):
        number += 1
        column -= 1
        if a == column and b == row:
            return number
    for i in range(1, level):
        number += 1
        row -= 1
        if a == column and b == row:
            return number
    for i in range(1, level):
        number += 1
        column += 1
        if a == column and b == row:
            return number
    
def decode(n):
    if n == 0:
        return (0, 0)
    if int(sqrt(n)) % 2 == 0:
        level = int(sqrt(n)) - 1
    elif int(sqrt(n)) % 2 == 1:
        level = int(sqrt(n))

    start_row = ((level - 1) // 2) * (-1)
    start_column = (level - 1) // 2 + 1
    row = start_row
    column = start_column
    number = level ** 2

    if n == number:
        return (start_column, start_row)
    
    for i in range(0, level):
        number += 1
        row += 1
        if number == n:
            return (column, row)
    for i in range(0, level + 1):
        number += 1
        column -= 1
        if number == n:
            return (column, row)
    for i in range(0, level + 1):
        number += 1
        row -= 1
        if number == n:
            return (column, row)
    for i in range(0, level + 1):
        number += 1
        column += 1
        if number == n:
            return (column, row)
s


