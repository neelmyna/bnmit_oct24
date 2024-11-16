import pandas as pd

players = {'Player':['sachin', 'kumble', 'srinath', 'dravid', 'sehwag', 'bumra', 'agarkar'], 'Team' : ['mi', 'csk', 'kkr', 'rcb', 'mi', 'csk', 'dd'], 'Price' : [10, 2, 2, 3, 5, 4, 6], 'Type' : ['batsman', 'bowler', 'bowler', 'batsman', 'batsman', 'bowler', 'bowler'], 'Run' : [1000, 150, 125, 950, 900, 90, 450], 'Wicket' : [20, 85, 83, 12, 35, 80, 90] }

df = pd.DataFrame(players)
print(df)
print('-' * 30)
print(df.iloc[:2,:])
print('-' * 30)
print(df.iloc[2:,:])
print('-' * 30)
print(df.iloc[-3:,:])
print('-' * 30)
print(df.iloc[2:-1,:1])

