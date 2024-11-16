import pandas as pd

names = pd.Series(['Asha', 'Ashok', 'Anupama', 'Aaraadhya'])

ages = pd.Series([19, 22, 21, 20])
branches = pd.Series(['CSE', 'AIML', 'ISE', 'ECE'])

data = {'Name' : names, 'Age' : ages, 'Branch' : branches}

studentf1 = pd.DataFrame(data)
#print(data)
print(studentf1)
print('-' * 30)

'''
studentf2 = studentf1.sort_values(by='Age')
print(studentf2)

studentf3 = studentf1.sort_values(by='Name')
print(studentf3)
'''

studentf4 = studentf1.sort_values(by='Name', ascending=0)
print(studentf4)