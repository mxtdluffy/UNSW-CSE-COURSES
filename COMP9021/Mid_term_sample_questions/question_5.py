

def f(word):
    '''
    Recall that if c is an ascii character then ord(c) returns its ascii code.
    Will be tested on nonempty strings of lowercase letters only.

    >>> f('x')
    The longest substring of consecutive letters has a length of 1.
    The leftmost such substring is x.
    >>> f('xy')
    The longest substring of consecutive letters has a length of 2.
    The leftmost such substring is xy.
    >>> f('ababcuvwaba')
    The longest substring of consecutive letters has a length of 3.
    The leftmost such substring is abc.
    >>> f('abbcedffghiefghiaaabbcdefgg')
    The longest substring of consecutive letters has a length of 6.
    The leftmost such substring is bcdefg.
    >>> f('abcabccdefcdefghacdef')
    The longest substring of consecutive letters has a length of 6.
    The leftmost such substring is cdefgh.
    '''
    desired_length = 0
    desired_substring = ''
    # Insert your code here
    str_list = []
    for i in word:
        str_list.append(ord(i))

    idx = 0
    idx_list = []
    str_length = []
    while idx < len(str_list):
        length = 1
        while idx < len(str_list) - 1:
            if str_list[idx] + 1 == str_list[idx + 1]:
                idx += 1
                length += 1
            else:
                idx_list.append(idx)
                str_length.append(length)
                break
        idx += 1
    if len(idx_list) == 0 or (not idx_list[-1] == len(str_list) - 1):
        idx_list.append(idx)
        str_length.append(length)

    desired_length = max(str_length)
    rcd = str_length.index(desired_length)
    desired_substring = word[idx_list[rcd] - desired_length - 1:idx_list[rcd]]
        
        
    
    print(f'The longest substring of consecutive letters has a length of {desired_length}.')
    print(f'The leftmost such substring is {desired_substring}.')
    
f('x')
f('xy')
f('ababcuvwaba')
f('abbcedffghiefghiaaabbcdefgg')
f('abcabccdefcdefghacdef')
'''
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    '''
