# Finds all triples of consecutive positive three-digit integers
# each of which is the sum of two squares.


# Insert you code here
def all_possible_integers():
    integer_dict = dict()
    for i in range(32):
        for j in range(i, 32):
            if i ** 2 + j ** 2 >= 100 and i ** 2 + j ** 2 < 1000:
                integer_dict[i ** 2 + j ** 2] = [i, j]
    all_integers = sorted(integer_dict.items(), key = lambda integer_dict: integer_dict[0])
    return all_integers

def find_three_consecutive_numbers(all_integers):
    solutions = []
    for i in range(len(all_integers) - 2):
        if all_integers[i][0] + 1 == all_integers[i + 1][0] and \
           all_integers[i + 1][0] + 1 == all_integers[i + 2][0]:
            solutions.append([[all_integers[i][0], all_integers[i + 1][0], \
                               all_integers[i + 2][0]], [all_integers[i][1], \
                               all_integers[i + 1][1], all_integers[i + 2][1]]])                                                    
    return solutions

def display(solutions):
    for element in solutions:
        print(f'({element[0][0]}, {element[0][1]}, {element[0][2]}) (equal to ' + \
              f'({element[1][0][0]}^2+{element[1][0][1]}^2, {element[1][1][0]}^2+' + \
              f'{element[1][1][1]}^2, {element[1][2][0]}^2+{element[1][2][1]}^2)) is a solution.')


all_integers = all_possible_integers()
# print(all_integers)
all_solutions = find_three_consecutive_numbers(all_integers)
# print(all_solutions)
display(all_solutions)
