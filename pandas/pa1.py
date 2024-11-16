import pandas as pd

my_data = pd.Series([2, 3, 5, 7, 9, 10, 12, 15])
print(my_data.head()) # by default prints 5 elements with its indices and dtype

print(my_data.head(2)) # prints only 1st 2 elements with the information

