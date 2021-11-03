#Getting Started

### Import pandas package
to use pandas, pandas package must import 
import pandas as pd

### Each column in a DataFrame is a Series
For example, 
![dataframe](https://pandas.pydata.org/docs/_images/01_table_spreadsheet.png)
if only 'Age' column is intested, you can only read one series
df["Age"]

out put - 
0	22
1	35
2	58


you can create a Series from scratch as well:
ages = pd.Series([22, 35, 58], name="Age")

out put -
0       22
1       35
2       58

**Note** - A pandas Series has no column labels, as it is just a single column of a DataFrame. A Series does have row labels


