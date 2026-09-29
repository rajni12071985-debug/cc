import pandas as pd 
import numpy as np 
import plotly.express as px 

import plotly.graph_objects as go 


 
print(df)
print(df.info())
print(df.isnull().sum())

print(df.describe())

print(df.columns)

sex = df["Sex"].value_counts().reset_index()
print(sex)

#fig = px.bar(sex , x = "Sex" , y = "count")
#fig.show()

job_title = df["Job Title"].value_counts().reset_index()

print(df["Job Title"].value_counts().reset_index())

#fig = px.bar(job_title , x = "Job Title" , y= "count")
#fig.show()
dob = df["Date of birth"].value_counts().reset_index()

ttt = df.groupby("First Name")["Date of birth"].value_counts().head(50)

print(ttt)

#fig = px.bar(ttt , x = "First Name" , y = "Date of birth")

#fig.show()

df["Date of birth"] = pd.to_datetime(df["Date of birth"])
print(df["Date of birth"].dt.year)

df["Birth year"] = df["Date of birth"].dt.year

Birth_year_count = df["Birth year"].value_counts().reset_index().sort_index()

print(Birth_year_count)

#fig = px.bar(Birth_year_count , x="Birth year" , y = "count")
#fig.show()


#fig = px.pie(sex , names="Sex" , values="count" , title = "Gender Distribution")
#fig.show()

#fig = px.histogram(df , x = "Date of birth" ,title="Distribution of Birth Years")
#fig.show()


job_title = df["Job Title"].value_counts().reset_index().head(10)

print(df["Job Title"].value_counts().reset_index().head(10))

#fig = px.bar(job_title , x = "Job Title" , y = "count")
#fig.show()

print(df["Job Title"].unique())

print(df.sort_values("Birth year" , ascending = False))

