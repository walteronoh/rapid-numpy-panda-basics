import pandas as pd
# Panda is a python library used for working with data sets
# It has functions for analyzing, cleaning, exploring, and manipulating data.

print("------------------------------------------SERIES----------------------------------------------------")
# Panda series - A one-dimensional array holding data of any type.

x1 = [1,2,3,4,5]
print(pd.Series(x1))

# Index from the series are labels
# Naming your own labels

x2 = x1
print("--Named labels--")
print(pd.Series(x2, index = ["a", "b", "c", "d", "e"]))

# Using key/value objects as series
x3 = { "day1" : 1, "day2": 2}
print("--Key/Value object series--")
print(pd.Series(x3))
# You can also specify the elements you want from the series
print("--Specified elements--")
print(pd.Series(x3, index = ["day2"]))

print("------------------------------------------DATAFRAMES----------------------------------------------------")
# DataFrames - multi-dimensional tables (2 dimensional data structure)
# Series is like a column, a DataFrame is the whole table.
dataset= {
    "animals": ["Cat", "Dog"],
    "colors" : ["brown", "white"]
}

x4 = pd.DataFrame(dataset)

print(x4)


print("--Locate rows--")
print("--Get a single row--")
print(x4.loc[0])

print("--Get a multiple rows--")
print(x4.loc[[0,1]])

print("-----------Named indexes---------")
dataset1 = dataset
x5 = pd.DataFrame(dataset1, index = ["a", "c"])
print(x5)

print("------------------------------------------READ CSV FILES----------------------------------------------------")
dataset2 = pd.read_csv("files/data.csv")
# print(dataset2.to_string())
# The head() method returns the headers and a specified number of rows, starting from the top.
print("-----------Info---------")
# info() gives you more information about a given dataset
print(dataset2.info())
print("-----------Head---------")
print(dataset2.head(30))
# The tail() method returns the headers and a specified number of rows, starting from the bottom.
print("-----------Tail---------")
print(dataset2.tail(3))

print("------------------------------------------READ JSON FILES----------------------------------------------------")
dataset3 = pd.read_json("files/data.json")
print("-----------Info---------")
print(dataset3.info())
print(dataset3.to_string())

print("------------------------------------------CLEANING DATA----------------------------------------------------")
# Fixing bad data in your dataset
# Due to: wrong data, Empty cells, wrong formats, duplicates
print("-------------------------------Removing Empty cells---------------------------------------")
# Removing rows that contain empty cells
dataset4 = dataset2.dropna() # Using dataset2.dropna(inplace=True), will change the original dataframe
# You can use subset when removing cells dataset2.dropna(subset=['column name']),
print(dataset4.to_string())

print("-------------------------------Replacing empty cells--------------------------------------")
dataset5 = dataset2.fillna("generated value") # Using dataset2.fillna("value", inplace=True), will change the original dataframe
print(dataset5.to_string())

print("---Replacing only for specified columns---")
dataset6 = dataset2["satisfaction_level"].fillna("specified column")
print(dataset6.to_string())

print("---------Replacing using Mean, Median, or Mode-------------")
print("-----Using Mean------")
dataset7 = dataset2["satisfaction_level"].fillna(dataset2["satisfaction_level"].mean())
print(dataset7.to_string())
print("-----Using Median------")
dataset7 = dataset2["satisfaction_level"].fillna(dataset2["satisfaction_level"].median())
print(dataset7.to_string())
print("-----Using Mode------")
dataset7 = dataset2["satisfaction_level"].fillna(dataset2["satisfaction_level"].mode()[0])
print(dataset7.to_string())

print("------------------------------------Cleaning Data of Wrong Format------------------------------------")
print("----------------Convert Into a Correct Format----------------------------")
# use pd.to_numeric(column), pd.to_datetime(column)
dataset8 = pd.to_numeric(dataset2["Emp ID"])
print(dataset8.to_string())

print("------------------------------------Cleaning Wrong Data------------------------------------")
print("---Replacing data---")
dataset9 = dataset2.copy()
for i in dataset9.index:
    if dataset9.loc[i, "Emp ID"] < 0:
        dataset9.loc[i, "Emp ID"] = 56

print(dataset9.to_string())

print("---Removing data---")
dataset10 = dataset2.copy()
for i in dataset10.index:
    if dataset10.loc[i, "Emp ID"] < 1:
        dataset10.drop(i, inplace=True)

print(dataset10.to_string())

print("------------------------------------Removing duplicates------------------------------------")
dataset11 = dataset2.copy()
# dataset11.duplicated() # Find duplicate cells, returns true/false
dataset11.drop_duplicates(subset=["last_evaluation"],inplace=True)
print(dataset11.to_string())
