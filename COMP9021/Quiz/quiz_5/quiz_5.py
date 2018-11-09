# Prompts the user for a nonnegative integer that codes a set S as follows:
# - Bit 0 codes 0
# - Bit 1 codes -1
# - Bit 2 codes 1
# - Bit 3 codes -2
# - Bit 4 codes 2
# - Bit 5 codes -3
# - Bit 6 codes 3
# ...
# Computes a derived nonnegative number that codes the set of running sums
# of the members of S when those are listed in increasing order.
#
# Computes the ordered list of members of a coded set.
#
# Written by Jingyun Shen and Eric Martin for COMP9021


import sys

try:
    encoded_set = int(input('Input a nonnegative integer: '))
    if encoded_set < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
        
def display(L):
    print('{', end = '')
    print(', '.join(str(e) for e in L), end = '')
    print('}')

def decode(encoded_set):
    decode_set = []
    binary_str = bin(encoded_set)[2:]
    bits = [0] * len(binary_str)
    cur = 1
    cnt = 1
    while cnt < len(binary_str):
        if cnt % 2 == 1:
            bits[-1 - cnt] = -1 * cur
            cnt += 1
        elif cnt % 2 == 0:
            bits[-1 - cnt] = cur
            cur += 1
            cnt += 1

    for i in range(len(binary_str)):
        if binary_str[i] == '1':
            decode_set.append(bits[i])

    decode_set = sorted(decode_set)        
    return decode_set
    
    
def code_derived_set(encoded_set):
    derived_set = []
    decode_set = decode(encoded_set)
    code_of_derived = 0
    tmp = 0
    for i in range(len(decode_set)):
        tmp += decode_set[i]
        derived_set.append(tmp)
    derived_set = sorted(list(set(derived_set)))

    for i in range(len(derived_set)):
        if derived_set[i] < 0:
            code_of_derived += 2 ** (- derived_set[i] * 2 - 1)
        else:
            code_of_derived += 2 ** (derived_set[i] * 2)
            
    return code_of_derived
    # REPLACE RETURN 0 ABOVE WITH YOUR CODE 

print('The encoded set is: ', end = '')
display(decode(encoded_set))
code_of_derived_set = code_derived_set(encoded_set)
print('The derived set is encoded as:', code_of_derived_set)
print('It is: ', end = '')
display(decode(code_of_derived_set))

    
