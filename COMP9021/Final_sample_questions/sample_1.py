
def remove_consecutive_duplicates(word):
    '''
    >>> remove_consecutive_duplicates('')
    ''
    >>> remove_consecutive_duplicates('a')
    'a'
    >>> remove_consecutive_duplicates('ab')
    'ab'
    >>> remove_consecutive_duplicates('aba')
    'aba'
    >>> remove_consecutive_duplicates('aaabbbbbaaa')
    'aba'
    >>> remove_consecutive_duplicates('abcaaabbbcccabc')
    'abcabcabc'
    >>> remove_consecutive_duplicates('aaabbbbbaaacaacdddd')
    'abacacd'
    '''
    # Insert your code here (the output is returned, not printed out)
    length = len(word)
    idx = 0
    result = ''
    if not length:
        return result
    if length == 1:
        return word
    while idx < length - 1:
        cur = word[idx]
        while idx < length - 1:
            if word[idx + 1] == cur:
                idx += 1
            else:
                break
        result += cur
        idx += 1
    if idx == length - 1:
        if cur != word[idx]:
            result += word[idx]
    return result
    
'''
if __name__ == '__main__':
    import doctest
    doctest.testmod()
'''
print(remove_consecutive_duplicates(''))
print(remove_consecutive_duplicates('a'))
print(remove_consecutive_duplicates('ab'))
print(remove_consecutive_duplicates('aba'))
print(remove_consecutive_duplicates('aaabbbbbaaa'))
print(remove_consecutive_duplicates('abcaaabbbcccabc'))
print(remove_consecutive_duplicates('aaabbbbbaaacaacdddd'))
