'''
Uses the Stack interface to evaluate an arithmetic expression written in postfix
and built from natural numbers using the binary +, -, * and / operators.             
'''


import re
from operator import add, sub, mul, truediv

from stack_adt import Stack, EmptyStackError


def evaluate(expression):
    '''
    Checks whether an expression is a valid fully parentherised infix expression,
    and in case the answer is yes, returns the value of the expression,
    provided that no division by 0 is attempted; otherwise, return None.

    >>> evaluate('100')
    100
    >>> evaluate('[(1 - 20) + 300]')
    281
    >>> evaluate('[1 - {20 + 300}]')
    -319
    >>> evaluate('( { 20*4 }/5 )')
    16.0
    >>> evaluate('(20*[4/5])')
    16.0
    >>> evaluate('({1 + (20 * 30)} - [400 / 500])')
    600.2
    >>> evaluate('{1 + [((20*30)-400) / 500]}')
    1.4
    >>> evaluate('[1 + {(2 * (3+{4*5})) / ([6*7]-[8/9]) }]')
    2.1189189189189186
    >>> evaluate('100 + 3')
    >>> evaluate('(100 + 3')
    >>> evaluate('(100 + -3)')
    >>> evaluate('(100 \ 50)')
    >>> evaluate('(100 / 0)')    
    '''
    if any(not (c.isdigit() or c.isspace() or c in '(){}[]+-*/') for c in expression):
        return
    # Tokens can be natural numbers, +, -, *, and /
    tokens = re.compile('(\d+|\(|\)|\[|\]|{|}|\+|-|\*|/)').findall(expression)
    try:
        value = evaluate_expression(tokens)
        return value
    except ZeroDivisionError:
        return

def evaluate_expression(tokens):
    stack = Stack()
    oppo_brace = {')': '(', ']': '[', '}': '{'}
    for token in tokens:
        if not (token == ')' or token == ']' or token == '}'):
            if not (token == '(' or token == '[' or token == '{' \
                    or token == '+' or token == '-' or token == '*' \
                    or token == '/'):
                    token = int(token)
                    stack.push(token)
            else:
                    stack.push(token)
        else:
            oppo = oppo_brace[token]
            try:
                arg_3 = stack.pop()
                arg_2 = stack.pop()
                arg_1 = stack.pop()
                arg = stack.pop()
                if arg != oppo:
                    return
            except EmptyStackError:
                    return
            
            stack.push({'+': add, '-': sub, '*': mul, '/': truediv}[arg_2](arg_1, arg_3))
    if stack.is_empty():
        return
    value = stack.pop()
    if not stack.is_empty():
        return
    return value
                    
    '''
        try:
            token = int(token)
            stack.push(token)
        except ValueError:
            try:
                arg_2 = stack.pop()
                arg_1 = stack.pop()
                stack.push({'+': add, '-': sub, '*': mul, '/': truediv}[token](arg_1, arg_2))
            except EmptyStackError:
                return
    if stack.is_empty():
        return
    value = stack.pop()
    if not stack.is_empty():
        return
    return value
    '''

if __name__ == '__main__':
    import doctest
    doctest.testmod()


