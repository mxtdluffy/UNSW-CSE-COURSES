'''
Tries and find a word in a text file that represents a grid of words, all of the same length.
There is only one word per line in the file.
The letters that make up a word can possibly be separated by an arbitrary number of spaces,
and there can also be spaces at the beginning or at the end of a word,
and there can be lines consisting of nothing but spaces anywhere in the file.
Assume that the file stores data as expected.

A word can be read horizontally from left to right,
or vertically from top to bottom,
or diagonally from top left to bottom right
(this is more limited than the lab exercise).
The locations are represented as a pair (line number, column number),
starting the numbering with 1 (not 0).
'''


def find_word(filename, word):
    '''
    >>> find_word('word_search_1.txt', 'PLATINUM')
    PLATINUM was found horizontally (left to right) at position (10, 4)
    >>> find_word('word_search_1.txt', 'MANGANESE')
    MANGANESE was found horizontally (left to right) at position (11, 4)
    >>> find_word('word_search_1.txt', 'LITHIUM')
    LITHIUM was found vertically (top to bottom) at position (2, 14)
    >>> find_word('word_search_1.txt', 'SILVER')
    SILVER was found vertically (top to bottom) at position (2, 13)
    >>> find_word('word_search_1.txt', 'SODIUM')
    SODIUM was not found
    >>> find_word('word_search_1.txt', 'TITANIUM')
    TITANIUM was not found
    >>> find_word('word_search_2.txt', 'PAPAYA')
    PAPAYA was found diagonally (top left to bottom right) at position (1, 9)
    >>> find_word('word_search_2.txt', 'RASPBERRY')
    RASPBERRY was found vertically (top to bottom) at position (5, 14)
    >>> find_word('word_search_2.txt', 'BLUEBERRY')
    BLUEBERRY was found horizontally (left to right) at position (13, 5)
    >>> find_word('word_search_2.txt', 'LEMON')
    LEMON was not found
    '''
    with open(filename) as file:
        grid = []
        # Insert your code here
        for line in file:
            each_line = list(filter(None, line.split(' ')))
            each_line[-1] = each_line[-1][:-1]
            if each_line[0] == '':
                continue
            else:
                while '' in each_line:
                    each_line.remove('')
                tmp = ''
                for char in each_line:
                    tmp += char
                grid.append(tmp)
        
        # A one liner that sets grid to the appropriate value is enough.
        location = find_word_horizontally(grid, word)
        found = False
        if location:
            found = True
            print(word, 'was found horizontally (left to right) at position', location)
        location = find_word_vertically(grid, word)
        if location:
            found = True
            print(word, 'was found vertically (top to bottom) at position', location)
        location = find_word_diagonally(grid, word)
        if location:
            found = True
            print(word, 'was found diagonally (top left to bottom right) at position', location)
        if not found:
            print(word, 'was not found')
    
    
def find_word_horizontally(grid, word):
    # Replace pass above with your code
    length = len(word)  
    row = len(grid)
    column = len(grid[0])

    for i in range(row):
        for j in range(column):
            if grid[i][j] == word[0]:
                if j + length - 1 > column - 1:
                    continue
                else:
                    tmp = grid[i][j: j + length]
                    if tmp == word:
                        return (i + 1, j + 1)
    return 

def find_word_vertically(grid, word):
    # Replace pass above with your code
    length = len(word)  
    row = len(grid)
    column = len(grid[0])
    for j in range(column):
        for i in range(row):
            if grid[i][j] == word[0]:
                if i + length - 1 > row - 1:
                    continue
                else:
                    tmp = ''
                    for k in range(length):
                        tmp += grid[i + k][j]
                    if tmp == word:
                        return (i + 1, j + 1)
    return

    
def find_word_diagonally(grid, word):
    # Replace pass above with your code
    length = len(word)  
    row = len(grid)
    column = len(grid[0])

    for i in range(row):
        for j in range(column):
            if grid[i][j] == word[0]:
                if j + length - 1 > column - 1 or i + length - 1 > row - 1:
                    continue
                else:
                    tmp = ''
                    for k in range(length):
                        tmp += grid[i + k][j + k]
                    if tmp == word:
                        return (i + 1, j + 1)

'''
if __name__ == '__main__':
    import doctest
    doctest.testmod()
'''
find_word('word_search_1.txt', 'PLATINUM')
find_word('word_search_1.txt', 'MANGANESE')
find_word('word_search_1.txt', 'LITHIUM')
find_word('word_search_1.txt', 'SILVER')
find_word('word_search_1.txt', 'SODIUM')
find_word('word_search_1.txt', 'TITANIUM')
find_word('word_search_2.txt', 'PAPAYA')
find_word('word_search_2.txt', 'RASPBERRY')
find_word('word_search_2.txt', 'BLUEBERRY')
find_word('word_search_2.txt', 'LEMON')
