# Prompts the user for a strictly positive number N
# and outputs an equilateral triangle of height N.
# The top of the triangle (line 1) is labeled with the letter A.
# For all nonzero p < N, line p+1 of the triangle is labeled
# with letters that go up in alphabetical order modulo 26
# from the beginning of the line to the middle of the line,
# starting wth the letter that comes next in alphabetical order
# modulo 26 to the letter in the middle of line p,
# and then down in alphabetical order modulo 26
# from the middle of the line to the end of the line.


# Insert your code here
height = int(input('Enter strictly positive number: '))

def display(height):
    all_char = []
    nb_of_char = 0
    idx = 0
    
    for i in range(1, height + 1):
        nb_of_char += i

    for j in range(0, nb_of_char):
        all_char.append(chr(65 + j % 26))
        
    for nb in range(1, height + 1):
        tmp = ''
        reverse_tmp = ''
        for cur1 in range(nb):
            tmp += all_char[idx + cur1]
        for cur2 in range(2, nb + 1):
            reverse_tmp += tmp[- cur2]
            
        idx += nb
        print(' ' * (height - nb) + tmp + reverse_tmp)
        


display(height)
