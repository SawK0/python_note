import pandas as pd


# Read CSV file
df = pd.read_csv('../data_files/players_20.csv')

# Export df data to excel file
# **sheet_name** is named the dataframe instead of the default Sheet1. 
# By setting index=False, the row index labels are not saved in the spreadsheet

""" df.to_excel("../data_files/players_20.xlsx", sheet_name="players", index=False) """

df2 = pd.read_excel("../data_files/players_20.xlsx", sheet_name="players")

print(df2)

print(df)

# see the first 7 rows
print(df.head(7))

# see the last 7 rows
print(df.tail(7))

# check the datatypes of all columns
print(df.dtypes)

# show data columns
print(df.columns)

# show data summary info
print(df.info())

# show data shape
print(df.shape)

