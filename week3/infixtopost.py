def get_precedence(operator):
    if operator == '^':
        return 3
    elif operator in ['*', '/', '%']:
        return 2
    elif operator in ['+', '-']:
        return 1

def infix_to_postfix(infix_expr):
    postfix_expr = ''
    stack = []
    for char in infix_expr: # Read the i/p string char by char
        if char[-1] >= 'a' and char[-1] <= 'z': # if the char is an operand, add it to postfix expr
            postfix_expr += char
        elif char == '(': # if the char is opening paranthesis
            stack.append('(') # add it to the stack
        elif char == ')' and len(stack) > 0: # if closing parantheis
            while stack[-1] != '(': # pop all operators until '('
                postfix_expr += stack.pop()
            stack.pop() # remove the '(' also
        else: # if the char is an operator
            while (not len(stack) == 0) and get_precedence(char) < get_precedence(stack[-1]) or (not len(stack) == 0) and get_precedence(stack[-1] == get_precedence(char)):
                postfix_expr += stack.pop()
            stack.append(char)
        while not len(stack) == 0: # copy remaining content from the stack to the postfix expr
            postfix_expr += stack.pop()

infix_expr = input('Enter the infix notation expression: ')
postfix_expr = infix_to_postfix(infix_expr)
print(f'Postfix Expression = {postfix_expr}')