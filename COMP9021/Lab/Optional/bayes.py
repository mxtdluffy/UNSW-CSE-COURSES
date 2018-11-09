'''
Simulates the cast of an unknown die, chosen from a set of 5 dice with 4, 6, 8, 12, and 20 sides.

To start with, every die has a probability of 0.2 to be the chosen die.
At every cast, the probability of each die is updated using Bayes' rule.
The probabilities are displayed for at most 6 casts.
If more than 6 casts have been requested, the final probabilities obtained
for the chosen number of casts are eventually displayed.
'''
'''
Enter the seed: 1
Enter the desired number of times a randomly chosen die will be cast: 5

This is a secret, but the chosen die is the one with 6 faces

Casting the chosen die... Outcome: 5
The updated dice probabilities are:
4: 0.00%
6: 39.22%
8: 29.41%
12: 19.61%
20: 11.76%

Casting the chosen die... Outcome: 1
The updated dice probabilities are:
4: 0.00%
6: 52.56%
8: 29.57%
12: 13.14%
20: 4.73%

Casting the chosen die... Outcome: 3
The updated dice probabilities are:
4: 0.00%
6: 63.54%
8: 26.80%
12: 7.94%
20: 1.72%

Casting the chosen die... Outcome: 1
The updated dice probabilities are:
4: 0.00%
6: 72.10%
8: 22.81%
12: 4.51%
20: 0.58%

Casting the chosen die... Outcome: 4
The updated dice probabilities are:
4: 0.00%
6: 78.68%
8: 18.67%
12: 2.46%
20: 0.19%


#####The final probabilities are:
4: 99.97%
6: 0.03%
8: 0.00%
12: 0.00%
20: 0.00%

'''
from random import choice, seed,randint



# pos_of_outcome[i] represents the posibility of obtaining outcome i
pos_of_outcome = [0] * 21

# Initialize pos_of_outcome
for i in range(1, 21):
    if i <= 4:
        pos_of_outcome[i] = 0.2 * (1/4 + 1/6 + 1/8 + 1/12 + 1/20)
    elif i <= 6:
        pos_of_outcome[i] = 0.2 * (1/6 + 1/8 + 1/12 + 1/20)
    elif i <= 8:
        pos_of_outcome[i] = 0.2 * (1/8 + 1/12 + 1/20)
    elif i <= 12:
        pos_of_outcome[i] = 0.2 * (1/12 + 1/20)
    else:
        pos_of_outcome[i] = 0.2 * 1/20
        
try:
    for_seed = int(input('Enter the seed: '))
    seed(for_seed)
    # break
except ValueError:
    pass

# Insert your code here
# Use choice() again when casting the die.

try:
    times = int(input('Enter the desired number of times a randomly chosen die will be cast: '))
    if times < 0:
        raise ValueError
except ValueError:
    print('Invalid time!')
    
dice = 4, 6, 8, 12, 20
chosen_dice = choice(dice)
dice_face = list(range(1, chosen_dice + 1))

print(f'\nThis is a secret, but the chosen die is the one with {chosen_dice} faces')

each_outcome = []
# [0] = P(chosen die = 4) [1] = ... 6 [2] = ...8
# [3] = ...12 [4] = ... 20
result_dice = [True] * 5
possibility = [0] * 5
output_pos = [0.00] * 5
cnt = 0

for i in range(times):
    # outcome = choice(all_dice[chosen_dice])
    outcome = choice(dice_face)

    each_outcome.append(outcome)
    if outcome > 4:
        result_dice[0] = False
    if outcome > 6:
        result_dice[1] = False
    if outcome > 8:
        result_dice[2] = False
    if outcome > 12:
        result_dice[3] = False
    
    p = 1
    for j in range(len(each_outcome)):
        p *= pos_of_outcome[each_outcome[j]]

    for cur_dice in range(5):
        if not result_dice[cur_dice]:
            possibility[cur_dice] = 0
        else:
            possibility[cur_dice] = 0.2 * (1 / (dice[cur_dice]) ** len(each_outcome)) / p
                        
    if i > 5:
        continue
    elif i < 5:
        print('\nCasting the chosen die... Outcome:', outcome)
        print('The updated dice probabilities are:')
        sum_pos = 0
        for index in range(5):
            sum_pos += possibility[index]
        for index in range(5):
            print(f'{dice[index]:6d}: {possibility[index] * 100 / sum_pos:.2f}%')

if times >= 5:
    sum_pos = 0
    for index in range(5):
        sum_pos += possibility[index]
    print('\nThe final probabilities are:')
    for index in range(5):
        print(f'{dice[index]:6d}: {possibility[index] * 100 / sum_pos:.2f}%')    
        

