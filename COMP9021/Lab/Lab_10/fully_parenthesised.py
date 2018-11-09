
import re

from stack_adt import Stack, EmptyStackError
from binary_tree_adt import BinaryTree


'''
Uses the Stack and BinaryTree interfaces to build an expression tree and evaluate
an arithmetic expression written in infix, fully parenthesised with parentheses,
brackets and braces, and built from natural numbers using the binary +, -, * and / operators.
'''


def parse_tree(expression):
    if any(not (c.isdigit() or c.isspace() or c in '(){}[]+-*/') for c in expression):
            return
    # Tokens can be natural numbers, +, -, *, and /
    tokens = re.compile('(\d+|\(|\)|\[|\]|{|}|\+|-|\*|/)').findall(expression)
    try:
        value = parse_expression(tokens)
        return value
    except ZeroDivisionError:
        return


def parse_expression(tokens):
    # Replace pass above with your code, modified from the exercise:
    # Evaluate fully parenthetised expressions with a stack.
    stack = Stack()
    oppo_brace = {')': '(', ']': '[', '}': '{'}
    for token in tokens:
        if not (token == ')' or token == ']' or token == '}'):
            if not (token == '(' or token == '[' or token == '{' \
                    or token == '+' or token == '-' or token == '*' \
                    or token == '/'):
                    token = BinaryTree(int(token))
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
            
            #stack.push({'+': add, '-': sub, '*': mul, '/': truediv}[arg_2](arg_1, arg_3))
            parse_tree = BinaryTree(arg_2)
            parse_tree.left_node = arg_1
            parse_tree.right_node = arg_3
            stack.push(parse_tree)
    if stack.is_empty():
        return
    parse_tree = stack.pop()
    if not stack.is_empty():
        return
    return parse_tree


if __name__ == '__main__':
    import doctest
    doctest.testmod()


