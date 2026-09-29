import numpy as np 
import pandas as pd 
import plotly.graph_objects as go 
import plotly.express as px 


data = pd.read_csv("netflix.csv")

print(data)

print(data.describe())
print(data.info)



data.rename(columns={
    "ratinglevel":"rating_description",
    "ratingdescription":"rating_code"
},inplace=True)

print(data.columns)

print(data.isnull().sum())

print(data.shape)

# Total missing value

print(data.isnull().sum().sum())

Title = data.groupby("title")["rating"].value_counts()

print(Title)

rating = data["rating"].value_counts()
print(rating)

user_rating_score = data["user_rating_score"].value_counts()
print(user_rating_score)

user_rating_score = data["user_rating_score"].max()
print(user_rating_score)


user_rating_score = data["user_rating_score"].mean()
print(user_rating_score)


Title = data.groupby("title")["rating"].max()

print(Title)

top10_rating_title = data.sort_values("user_rating_score",ascending = False).value_counts()

print((top10_rating_title).head(10))


print(data["title"].nunique())

print(data["release_year"].min())

print(data["release_year"].max())


# HAr rating me kitne title hai 

Rating_title_No = data.groupby("rating")["title"].count()

print(Rating_title_No)

# kaunsi rating ke titles ka avg user_rating_score sabse high hai 

user_rating_score = data.groupby("rating")["user_rating_score"].mean().sort_values(ascending = False)

print(user_rating_score)

print(data["user_rating_score"].max())

print(data["user_rating_score"].value_counts())

print(data["user_rating_score"].value_counts().loc[99])

print(data[data["user_rating_score"]==99][["title", "user_rating_score"]])


print(data[data["release_year"] == 2017])

high_rated = data[data["user_rating_score"]>=90]

print(high_rated["release_year"].value_counts().sort_index())

#   visual question 1 

# kaunsi si rating category mein sabsejadha title hai 

rating_counts = data["rating"].value_counts().reset_index()

print(rating_counts)

#fig = px.bar(rating_counts, x = "rating" , y="count")
#fig.show()



