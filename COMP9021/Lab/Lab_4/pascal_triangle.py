# Prompts the user for a number N and prints out the first N + 1 lines of Pascal triangle.



# Insert you code here            
while True:
    try:
        N = int(input('Enter a nonnegative integer: '))
        if N < 0:
            raise ValueError
        break
    except ValueError:
        print('Incorrect input, try again')

def create_char_set(N):
    char_set = []
    if N == 0:
        char_set.append([1])
    elif N == 1:
        char_set.append([1])
        char_set.append([1, 1])
    else:
        char_set.append([1])
        char_set.append([1, 1])
        for cur in range(3, N + 2):
            tmp = [1]
            for i in range(cur - 2):
                tmp.append(char_set[-1][i] + char_set[-1][i + 1])
            tmp.append(1)
            char_set.append(tmp)
            
    return char_set

def find_max_bit(char_set):
    bit = []
    for nb in char_set[-1]:
        bit.append(len(str(nb)))
    max_bit = max(bit)
    return max_bit

def display(char_set):
    height = len(char_set)
    max_bit = find_max_bit(char_set)
    for i in range(height):
        tmp = ' ' * (height - i - 1) * max_bit
        for nb in range(len(char_set[i])):
            if not nb == len(char_set[i]) - 1:
                tmp += ' ' * (max_bit - len(str(char_set[i][nb]))) + str(char_set[i][nb]) +  ' ' * max_bit
            else:
                tmp += ' ' * (max_bit - len(str(char_set[i][nb]))) + str(char_set[i][nb])
        
        print(tmp)
              
    

all_char = create_char_set(N)
display(all_char)
