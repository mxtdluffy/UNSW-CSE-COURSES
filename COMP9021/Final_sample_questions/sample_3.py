'''
Given a word w, a good subsequence of w is defined as a word w' such that
- all letters in w' are different;
- w' is obtained from w by deleting some letters in w.

Returns the list of all good subsequences, without duplicates, in lexicographic order
(recall that the sorted() function sorts strings in lexicographic order).

The number of good sequences grows exponentially in the number of distinct letters in w,
so the function will be tested only for cases where the latter is not too large.

'''


def good_subsequences(word):
    '''
    >>> good_subsequences('')
    ['']
    >>> good_subsequences('aaa')
    ['', 'a']
    >>> good_subsequences('aaabbb')
    ['', 'a', 'ab', 'b']
    >>> good_subsequences('aaabbc')
    ['', 'a', 'ab', 'abc', 'ac', 'b', 'bc', 'c']
    >>> good_subsequences('aaabbaaa')
    ['', 'a', 'ab', 'b', 'ba']
    >>> good_subsequences('abbbcaaabccc')
    ['', 'a', 'ab', 'abc', 'ac', 'acb', 'b', 'ba', 'bac',\
 'bc', 'bca', 'c', 'ca', 'cab', 'cb']
    >>> good_subsequences('abbbcaaabcccaaa')
    ['', 'a', 'ab', 'abc', 'ac', 'acb', 'b', 'ba', 'bac',\
 'bc', 'bca', 'c', 'ca', 'cab', 'cb', 'cba']
    >>> good_subsequences('abbbcaaabcccaaabbbbbccab')
    ['', 'a', 'ab', 'abc', 'ac', 'acb', 'b', 'ba', 'bac',\
 'bc', 'bca', 'c', 'ca', 'cab', 'cb', 'cba']
    '''
    # Insert your code here
    char = ''
    length = len(word)
    idx = 0
    if not length:
        return ['']
    if length == 1:
        return ['', word]
    while idx < length - 1:
        cur = word[idx]
        while idx < length - 1:
            if word[idx + 1] == cur:
                idx += 1
            else:
                break
        char += cur
        idx += 1
    if idx == length - 1:
        if cur != word[idx]:
            char += word[idx]
            
    result = ['']
    tmp = ''
    for i in range(len(char)):
        tmp = char[i]
        solve(char[i + 1:], result, tmp)
    
    result = sorted(result)
    return result

# Possibly define another function
def solve(char, result, tmp):
    if tmp not in result:
        result.append(tmp)
    for i in range(len(char)):
        if char[i] not in tmp:
            new_tmp = tmp + char[i]
            solve(char[i + 1:], result, new_tmp)       

'''
if __name__ == '__main__':
    import doctest
    doctest.testmod()
'''
print(good_subsequences(''))
print(good_subsequences('aaa'))
print(good_subsequences('aaabbb'))
print(good_subsequences('aaabbc'))
print(good_subsequences('aaabbaaa'))
print(good_subsequences('abbbcaaabccc'))
print(good_subsequences('abbbcaaabcccaaa'))
print(good_subsequences('abbbcaaabcccaaabbbbbccab'))
