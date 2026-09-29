import pandas as pd 
import  plotly.express as px  
import numpy as np 
import plotly.graph_objects as go 

data = pd.read_csv("IPL.csv")
print(data.isnull().sum())
print(data.describe())

print(data.dtypes)

print(data.duplicated().sum())
missing_values = data[data.isnull().any(axis=1)]
print(data[data.isnull().any(axis=1)])

print(data.info())

print(data.shape[0])
print(data.shape[1])

print(data.columns)

print(data["team1"])
print(data.head(6))

print(data.dtypes)

print(data.duplicated().sum())

wins = data["match_winner"].value_counts()
print(data["match_winner"].value_counts())

print(wins.index)

print(wins.values)


#fig = px.bar(x = wins.index , y = wins.values , title = "IPL 2022 winner Analysis")
#fig.show()

matches_played =pd.concat([data["team1"] , data["team2"]]).value_counts()

print(matches_played)

Toss_win = data["toss_winner"].value_counts()

Toss_and_match_winner = data[data["toss_winner"] == data["match_winner"]]
Toss_and_match = data[data["toss_winner"] != data["match_winner"]]

toss_match_count = len(Toss_and_match_winner)

toss_not_match_count = len(Toss_and_match)

print(toss_match_count)
print(toss_not_match_count)

data["toss_loser"] = data.apply(
    lambda row : row["team2"] if
row["toss_winner"] == row["team1"]else
row["team1"]   ,
    axis = 1
)
toss_loss_but_win = data["toss_loser"].value_counts()
print(data["toss_loser"].value_counts())

toss_loss_match_winner = data[data["toss_loser"] == data["match_winner"]]
print(toss_loss_match_winner)

toss_loss_match_loss  = data[data["toss_loser"] != data["match_winner"]]
print(toss_loss_match_loss )

toss_loss_winner_count = len(toss_loss_match_winner)
toss_loss_win_loss = len(toss_loss_match_loss)

labels = ["Toss jit kr match jita" , "Toss jit kr match hara","Toss harkar match jita " , "Toss harkr match har gye "]
values = [toss_match_count,toss_not_match_count,toss_loss_winner_count,toss_loss_win_loss ]




#fig = px.pie(names = labels,values = values , title = "Toss Winner vs Match Winner")
#fig.show()

print(data["toss_decision"].value_counts())

field_win = data[(data["toss_decision"] == "Field" ) & (data["toss_winner"] == data["match_winner"])].value_counts()



Bat_win = data[(data["toss_decision"] == "Bat" ) & (data["toss_winner"] != data["match_winner"])].value_counts()

print(Bat_win)

print(data[["match_winner" , "player_of_the_match" , "venue"]].value_counts() )

group =data.groupby("team1")["first_ings_wkts"].mean()

print(group)
print(data[["first_ings_wkts" , "team1"]])