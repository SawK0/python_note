## My Pandas Note


### Install pandas
pip install pandas or conda install pandas 

### What kind of data does pandas handle?
- tabular data such as data stored in spreadsheets or databases. Pandas will help you to explore, clean, and process your data.

### How do I read and wirte tabular data?
- pandas supports the integration with many file formats (csv, excel, sql, json, parquet, ...). Importing data from each of these data sources is provided by function with prefix **read_***. Similarly, the **to_*** methods are used to store data
![read and write](https://pandas.pydata.org/docs/_images/02_io_readwrite.svg)


### How to create plots in pandas?
- pandas provides plottin using power of Matplotlib. 
![Matplotlib](https://pandas.pydata.org/docs/_images/04_plot_overview.svg)


### How to calculate summary statistics?
- Basic staistics are easily calculable in pandas.

### How to reshape the layout of tables
Change the structure of data table in multiple ways, **melt()** method can can wide to long/tidy form or **pivot()** from long to wide format.
![reshape the layout tables](https://pandas.pydata.org/docs/_images/07_melt.svg)



