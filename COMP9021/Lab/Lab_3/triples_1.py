# Finds all triples of positive integers (i, j, k) such that
# i, j and k are two digit numbers, i < j < k,
# every digit occurs at most once in i, j and k,
# and the product of i, j and k is a 6-digit number
# consisting precisely of the digits that occur in i, j and k.


# Insert your code here

def find_integer_pairs():
    integer_pairs = []
    for num1 in range(10, 100):
        for num2 in range(num1 + 1, 100):
            for num3 in range(num2 + 1, 100):
                num_of_digit = []
                for i in str(num1) + str(num2) + str(num3):
                    num_of_digit.append(i)
                num_of_digit = list(set(num_of_digit))
                if len(num_of_digit) == 6:
                    integer_pairs.append([num1, num2, num3])
    return integer_pairs

def if_product_satisfied(pairs, product):
    satisfied = False
    if not len(str(product)) == 6:
        return satisfied
    
    pairs_digits = []
    product_digits = []
    for i in range(3):
        for digit in str(pairs[i]):
            pairs_digits.append(digit)
    pairs_digits = sorted(pairs_digits)

    for digit in str(product):
        product_digits.append(digit)
    product_digits = sorted(list(set(product_digits)))

    if pairs_digits == product_digits:
        satisfied = True
            
    return satisfied

def satisfied_integer_pairs(integer_pairs):
    satisfied_pairs = []
    for pairs in integer_pairs:
        product = pairs[0] * pairs[1] * pairs[2]
        if if_product_satisfied(pairs, product):
            satisfied_pairs.append(pairs)
    return satisfied_pairs

def display(pair_set):
    for pairs in pair_set:
        print(f'{pairs[0]} x {pairs[1]} x {pairs[2]} = {pairs[0] * pairs[1] * pairs[2]} is a solution.')
    pass

integer_pairs = find_integer_pairs()
satisfied_pairs = satisfied_integer_pairs(integer_pairs)
display(satisfied_pairs)
