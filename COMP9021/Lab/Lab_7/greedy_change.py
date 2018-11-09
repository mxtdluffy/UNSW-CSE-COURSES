# Prompts the user for an amount, and outputs the minimal number of banknotes
# needed to match that amount, as well as the detail of how many banknotes
# of each type value are used.
# The available banknotes have a face value which is one of
# $1, $2, $5, $10, $20, $50, and $100.


# Insert your code here    
amount = int(input('Input the desired amount: '))

banknotes = [100, 50, 20, 10, 5, 2, 1]
result = [0, 0, 0, 0, 0, 0, 0]
for i in range(7):
    result[i] = amount // banknotes[i]
    amount = amount - banknotes[i] * result[i]

nb_of_notes = sum(result)
print()
if nb_of_notes > 1:
    print(f'{nb_of_notes} banknotes are needed.')
else:
    print(f'{nb_of_notes} banknote is needed.')
print('The detail is:')
for i in range(7):
    if result[i]:
        print(f'{"$" + str(banknotes[i]):>4}: {result[i]}')
