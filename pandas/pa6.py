import pandas as pd

dataf = pd.DataFrame({'asha': [20, 24, 21, 25], 'ashok': [19, 15, 21, 20], 'anupama' : [22, 19, 24, 25]})

print(dataf.iloc[:,: -1]) # print all column names except the last

print(dataf.iloc[: -2, : ]) # print all rows, except the last 2