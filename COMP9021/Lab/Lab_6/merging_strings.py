# Say that two strings s_1 and s_2 can be merged into a third
# string s_3 if s_3 is obtained from s_1 by inserting
# arbitrarily in s_1 the characters in s_2, respecting their
# order. For instance, the two strings ab and cd can be merged
# into abcd, or cabd, or cdab, or acbd, or acdb..., but not into
# adbc nor into cbda.
#
# Prompts the user for 3 strings and displays the output as follows:
# - If no string can be obtained from the other two by merging,
# then the program outputs that there is no solution.
# - Otherwise, the program outputs which of the strings can be obtained
# from the other two by merging.


# Insert your code here

string_1 = input('Please input the first string: ')
string_2 = input('Please input the second string: ')
string_3 = input('Please input the third string: ')


length_1 = len(string_1)
length_2 = len(string_2)
length_3 = len(string_3)

def find_solution(str_1, str_2, str_3):
    if not str_2 and str_1 == str_3:
        return True
    if not str_3 and str_1 == str_2:
        return True
    if not str_2 or not str_3:
        return False
    if str_1[0] == str_2[0] and find_solution(str_1[1:], str_2[1:], str_3):
        return True
    if str_1[0] == str_3[0] and find_solution(str_1[1:], str_2, str_3[1:]):
        return True
    return False
    
if length_1 == length_2 + length_3:
    if find_solution(string_1, string_2, string_3):
        print('The first string can be obtained by merging the other two.')
    else:
        print('No solution')
elif length_2 == length_1 + length_3:
    if find_solution(string_2, string_1, string_3):
        print('The second string can be obtained by merging the other two.')
    else:
        print('No solution')
elif length_3 == length_1 + length_2:
    if find_solution(string_3, string_1, string_2):
        print('The third string can be obtained by merging the other two.')
    else:
        print('No solution')
else:
    print('No solution')

    
    
