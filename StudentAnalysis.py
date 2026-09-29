import pandas as pd 
import numpy as np 
import plotly.express as px 
import plotly.graph_objects as go 


data = pd.read_csv("student-dataset.csv")

print(data)
print(data.describe())

print(data.isnull().sum())

print(data[["name","city"]].head(5))
math = data.groupby("gender")["math.grade"].max()
print(math)
print(data.info())
gender_count = data["gender"].value_counts()
print(data["gender"].value_counts())

#fig = px.bar(x =gender_count.index, y = gender_count.values, title = "GENDER ANALYSIS")

#fig.show()'

print(data["age"].max())
#fig = px.histogram(data , x = "age" , title = "Age Distribution of Students")
#fig.show()

city_wise_marks = data.groupby("gender")["math.grade"].mean()

print(city_wise_marks )

Female_math = data[data["gender"] == "F"].groupby("nationality")["math.grade"].max()

print(Female_math)

gender_math = data.groupby(["nationality" , "gender"])["math.grade"].mean()
print(gender_math)

print(data["city"].value_counts())

max_math_marks = data.loc[data["math.grade"].idxmax() ,["name","nationality"]]
max_english_marks = data.loc[data["english.grade"].idxmax() , "name"]
max_science_marks = data.loc[data["sciences.grade"].idxmax() , "name"]
max_language_marks = data.loc[data["language.grade"].idxmax() , "name"]

print(max_math_marks)
print(max_english_marks)
print(max_science_marks)
print(max_language_marks)


Country_math_score = data.groupby("nationality")["math.grade"].max()

print(Country_math_score)

  #Male vs Female Math Performance

male_female  = data.groupby("gender")["math.grade"].max()

print(male_female)

