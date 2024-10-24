import sys

print('User given numbers are: ', sys.argv)
numbers = []

for i in range(1, len(sys.argv)):
    numbers.append(int(sys.argv[i]))

print(f'User given numbers are: {numbers}')