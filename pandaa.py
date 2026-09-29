import pandas as pd

myDataset = {
    'car' : ["bmw " ,"audi" , "lamborgini"],
    'passing' : [3,4,5]
}

myData = pd.DataFrame(myDataset)

print(myData)
print(pd.__version__)


a = [1,7,2]

print(pd.Series(a , index = ["x" , "y" , "z"]))
print(a)



calories = {"day1"  : [12,3,4,56], "day2":[23,6,7,89], "day3":[34,45,12,34]}

print(pd.DataFrame(calories))




pd.options.display.max_rows=100
df = pd.read_csv('data.csv')

print(df)


df = pd.read_json('data.json')

print(df.head(10))