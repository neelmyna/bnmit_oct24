#Data frame example

import pandas as pd

dataf = pd.DataFrame({'asha': [20, 24, 21, 25], 'ashok': [19, 15, 21, 20], 'anupama' : [22, 19, 24, 25]})

print('Data Frame: \n', dataf)

print(dataf.idxmax(axis=0)) # returns the column names as 1st column in the Result and the row number as 2nd column in the result, at which the Max value is present for that particular column.

print(dataf.idxmax(axis=1)) # Returns 2 Coulmns in result. 1st is the row number and 2nd is the columns name.
# Returns the column name of the column with 1st max value.
