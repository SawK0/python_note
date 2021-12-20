import pandas as pd


"""To load the pandas package and start working with, import the package as above.
The community agree alias for pandas is pd
"""

# source from pandas documentation
# https://pandas.pydata.org/docs/getting_started/intro_tutorials/01_table_oriented.html

# To manually store data in a table, create DataFrame. When using Python dictionary of lists, the dictionary keys will be used as column headers 

df = pd.DataFrame(
    {
        "Name" : [
            "David",
            "Cathy",
            "Jack"
        ],
        "Age": [22, 19, 25],
        "Sex" : ["M", "F", "M"]
    }
)


#view data
print(df)

