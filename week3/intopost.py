class Infix_to_postfix:
    def __init__(self, input_expr='a+(b-c)*d^e'):
        self.top = -1 #initially the stack is empty
        self.length = len(input_expr)
        self.stack = [] # to store the operators
        self.postfix_expr = [] # to store the result
        self.precedence = {'^':3, '*':2, '/':2, '%':2, '+':1, '-':1}

    def is_stack_empty(self):
        return True if self.top == -1 else False
    
    def get_top(self):
        return self.stack[-1]
    
    def pop(self):
        if not self.is_stack_empty():
            self.top -= 1
            return self.stack.pop()
        else:
            return '@' # a dummy character
        
    def push(self, operator):
        self.top += 1
        self.stack.append(operator)
    
    def is_operand(self, char):
        return char.isalpha()

    def check_precedence(self, operator):
        try:
            curr_opr = self.precedence[operator]
            top_opr = self.precedence[self.get_top()]
            return True if curr_opr <= top_opr else False
        except KeyError:
            return False
        
    def infix_to_postfix(self, input_expr):
        for char in input_expr:
            if self.is_operand(char):
                self.postfix_expr.append(char)
            elif char == '(':
                self.push(char)
            elif char == ')':
                while not self.is_stack_empty() and self.get_top() != '(':
                    value1 = self.pop()
                    self.postfix_expr.append(value1)
                if not self.is_stack_empty() and self.get_top() != '(':
                    return -1 # postfix expr is fully built
                else: # pop the opening paranthesis from stack
                    self.pop() # remove the opening paranthesis from top of the stack
            else: # if the character is operator
                while not self.is_stack_empty() and self.check_precedence(char):
                    self.postfix_expr.append(self.pop())
                self.push(char)# push the curr operator on the stack if its precedence is bigger
        #once all chars are read from the input expr, check the stack, if it has elements in it.
        while not self.is_stack_empty():
            self.postfix_expr.append(self.pop())
        
        print(''.join(self.postfix_expr)) #print o/p as a string

input_expr = 'a+(b-c)*d^e-k'
in_to_post = Infix_to_postfix(input_expr)
in_to_post.infix_to_postfix(input_expr)



