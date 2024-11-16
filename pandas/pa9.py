import pandas as pd

df1 = pd.DataFrame({'roll-no':[123], 'name' : ['sowmya']})
df2 = pd.DataFrame({'roll-no':[124, 125], 'name' : ['ramya', 'sowjanya']})

df3 = df1.merge(df2, on='roll-no', how='outer')
print(df3)

df4 = df1.merge(df2, on='roll-no', how='right')
print(df4)

df5 = df1.merge(df2, on='roll-no', how='left')
print(df5)

df5 = df1.merge(df2, on='roll-no', how='inner')
print(df5)