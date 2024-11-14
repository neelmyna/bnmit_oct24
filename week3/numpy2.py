'''
Read N (Number of gold coins)
List of N intergers (specifying value of N Gold coins)
Read Q (The Number instructions each of which is either HARRY or REMOVE
Read X (The value at which the Monk will go to sleep)

Monk goes to sleep: The sum of gold coins in Monk's bag (Stack)
Print X as O/P
'''

n = int(input('Enter number of Gold coins: '))
coin_values = []

print(f'Enter values of {n} Gold coins')
for i in range(n):
    coin_values.append(int(input()))

q = int(input('Enter number of instructions: '))
instructions = list()

print(f'Enter the {q} instructions')
for i in range(q):
    instructions.append(input().strip().lower())

x = int(input('Enter value of X: '))

monk_stack = []
condition_met = False

print(coin_values, '\n', instructions)

j = 0
for i in range(0, q):
    if instructions[i] == 'harry' and i < len(coin_values):
        monk_stack.append(coin_values[j])
        j += 1
    elif instructions[i] == 'remove':
        monk_stack.pop()
    if sum(monk_stack) == x:
        condition_met = True
        break #break the loop

if condition_met:
    print(f'Number of coins = {len(monk_stack)}')
else:
    print('-1')
