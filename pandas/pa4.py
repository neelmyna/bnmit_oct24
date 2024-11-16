import pandas as pd

dataf = pd.DataFrame({'asha': [20, 24, 21, 25], 'ashok': [19, 15, 21, 20], 'anupama' : [22, 19, 24, 25]})

print(dataf.columns)
print(dataf[1:3])
print(dataf[:2])
print(dataf[1:])

