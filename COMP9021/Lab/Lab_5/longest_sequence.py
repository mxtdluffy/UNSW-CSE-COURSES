# Prompts the user for a string w of lowercase letters and outputs the
# longest sequence of consecutive letters that occur in w,
# but with possibly other letters in between, starting as close
# as possible to the beginning of w.


import sys


# Insert your code here
in_str = input('Please input a string of lowercase letters: ')
out_str = ''

length = len(in_str)

idx = 0
store = []
for i in range(length):
    tmp_str = in_str[i]
    cur_ord = ord(in_str[i])
    for j in range(i + 1, length):
        if ord(in_str[j]) == cur_ord + 1:
            cur_ord += 1
            tmp_str += in_str[j]
    store.append(tmp_str)
    

tmp_out = store[0]
for each_str in store:
    if len(each_str) > len(tmp_out):
        tmp_out = each_str
    
out_str = tmp_out


print('The solution is:', out_str)
