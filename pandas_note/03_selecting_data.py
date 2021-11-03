import pandas as pd

df = pd.read_csv("../data_files/players_20.csv")

print(df.columns)

# Select a column

print(df['short_name'])
print(df['short_name'].head())

# show the shape of a column
print(df["long_name"].shape)

# assign a varaible and store a column
name = df['long_name']
print(name.head(7))

# check column type. Each column dataframe is a series. 
print(type(name))

# if you want to check datatype of a column use dtypes instead
print(name.dtypes)


"""--------------------------------------------------------------"""

# select multiple columns
print(df[["short_name", "age"]])