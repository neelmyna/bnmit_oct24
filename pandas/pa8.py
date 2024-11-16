import pandas as pd

players = {'Player':['sachin', 'kumble', 'srinath', 'dravid', 'sehwag', 'bumra', 'agarkar', 'ganguly'], 'Team' : ['mi', 'csk', 'kkr', 'rcb', 'mi', 'csk', 'dd', 'kkr'], 'Price' : [10, 2, 2, 3, 5, 4, 6, 8], 'Type' : ['batsman', 'bowler', 'bowler', 'batsman', 'batsman', 'bowler', 'bowler', 'batsman'], 'Run' : [1000, 150, 125, 950, 900, 90, 450, 885], 'Wicket' : [20, 85, 83, 12, 35, 80, 90, 10] }

df = pd.DataFrame(players)

#Least expensive player. 
print(df[df['Price'] == df['Price'].min()])
# Create a DF out of existing DF with a condition and library method

# Print number of players bidded so far for each of the teams
print(df.groupby('Team').Player.count())

# Most expensive player. 
print(df[df['Price'] == df['Price'].max()])

# Sum of runs of each team
print(df.groupby(['Team']).Run.sum())

# Avg of runs of each team
print(df.groupby(['Team']).Run.mean())

# Sort players with their runs
print(df.sort_values(by='Run'))

# Sort players with their bidding price
print(df.sort_values(by='Price', ascending=0))

# Sort players according to their wickets
print(df.sort_values(by='Wicket', ascending=0))

# Highest priced player from each team
value = df.groupby('Team')
print(value['Player', 'Price'].max())
