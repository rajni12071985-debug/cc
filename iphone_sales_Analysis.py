import pandas as pd 
import numpy as np 
import plotly.express as px 
import plotly.graph_objects as go


data = pd.read_csv("apple_products.csv")

print(data.isnull().sum())

print(data.describe())

# Top 10 apple i phone brand 

Highest_rating = data.sort_values(by = ["Star Rating"] , ascending = False).head(10)
print(Highest_rating.head(10))

# Have a look  at  the number of rating of the highest rated i phone on flipkart

#iphones = Highest_rating["Product Name"].value_counts()
iphones = Highest_rating["Product Name"].value_counts()

lables = iphones.index
count = Highest_rating["Number Of Reviews"]

#figure = px.bar(Highest_rating , x = lables , y = count,  title = "Rating of Highest Rated iPhone")
#figure.show()


figure = px.scatter(data_frame = data , x = "Number Of Ratings" , y = "Sale Price" , size = "Discount Percentage", title = "Relationship btw sale $ rating")

figure.show()                         

#print(data)