'''
lst = [[c for c in range(r)] for r in range(3)]
for x in lst:
    for y in x:
        if y < 2:
            print('*', end='')

print(lst)
--------------------------
a = 'hello' # line 1
def x(a,b): # line 2
    z = a[0] # line 3
    return z # line 4
print(x(a)) # line 5
'''
'''
s = 'SPAM'
def f(x):
    return s + 'MAPS'
print(f(s))
'''

def my_function(*args):
    print(args)

my_function(10)
my_function(1, 2, 3,)
my_function()
my_function(10, [1, 2, 3], 'bnmit', 15)
