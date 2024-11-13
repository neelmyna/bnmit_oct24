list1 = [2, 3, 5]

string = ' '.join(map(str, list1)) # convert a list of items of tyep other than str into a string
print(string)
print(type(string))

list2 = ['23', '55', '67']
string = ' '.join(list2) 
print(string)