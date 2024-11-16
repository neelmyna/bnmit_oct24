import pandas as pd

dataf = pd.DataFrame({'asha': [20, 24, 21, 25], 'ashok': [19, 15, 21, 20], 'anupama' : [22, 19, 24, 25]})

print('Data Frame: \n', dataf)
print(dataf.idxmin(axis=0)) # returns 2 the result in 2 columns. 1st is the columns name and 2nd is the row number. The column name with the minimum value for its column is returned.

print(dataf.idxmin(axis=1))
