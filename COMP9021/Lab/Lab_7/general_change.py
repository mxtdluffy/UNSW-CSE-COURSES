'''
This program prompts the user for the face values of banknotes
and their associated quantities as well as for an amount, and
if possible, outputs the minimal number of banknotes needed to
match that amount, as well as the detail of how many banknotes
of each type value are used.

$ python3 general_change.py
Input pairs of the form ’value : number’
   to indicate that you have ’number’ many banknotes of face value ’value’.
Input these pairs one per line, with a blank line to indicate end of input.
1: 100
2: 5
3: 4
10:5
20:4
30:1
Input the desired amount: 107
There are 2 solutions:
 $1: 1
 $3: 2
$10: 1
$20: 3
$30: 1
$2: 2
 $3: 1
$10: 1
$20: 3
$30: 1

'''
print("Input pairs of the form 'value : number' to indicate that you have\n"
      "'number' many banknotes of face value 'value'.")
print('Input these pairs one per line, with a blank line '
      'to indicate end of input.\n')
face_values = []
while True:
    line = input()
    if ':' not in line:
        break
    value, quantity = line.split(':')
    face_values.append([int(value), int(quantity)])
# Might make the computation more efficient.
face_values.reverse()
nb_of_face_values = len(face_values)
amount = int(input('Input the desired amount: '))

def solve(left_values, left_amount, result):
    if left_amount == 0:
        result.append('T')
        return True
    
    no_solution = True
    for i in range(len(left_values)):
        if left_values[i][1] and left_values[i][0] <= left_amount:
            no_solution = False
            break
    if no_solution:
        result.append('F')
        return False
    
    for i in range(len(left_values)):
        if (not left_values[i][1] == 0) and left_amount >= left_values[i][0]:
            new_values = []
            for j in range(len(left_values)):
                if j == i:
                    new_values.append([left_values[j][0], left_values[j][1] - 1])
                else:
                    new_values.append([left_values[j][0], left_values[j][1]])
                    
            result.append(left_amount - left_values[i][0])
            
            if solve(new_values, left_amount - left_values[i][0]):
                result.append(left_amount - left_values[i][0])
    return

solve(face_values, amount)
print(result)
