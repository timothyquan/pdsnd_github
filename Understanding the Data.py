import pandas as pd

# Understanding the Data
# Let's use pandas to better understand the bike share data! Use this code editor to explore chicago.csv and answer the questions below. The file included here is a mini version of one of the actual data files you will work with for the project. It only includes 400 rows, but the structure and columns are the same.

# What columns are in this dataset?
# Are there any missing values?
# What are the different types of values in each column?
# Some useful pandas methods:

# df.head()
# df.columns
# df.describe()
# df.info()
# df['column_name'].value_counts()
# df['column_name'].unique()

#pd.set_option('display.max_rows', None)
df = pd.read_csv("Python\Explore US Bikeshare Data\chicago.csv")
print(df)  # start by viewing the first few rows of the dataset!
print('What columns are in this dataset?')
print(df.columns.tolist())
print('Are there any missing values?')
print('The following rows contain missing values: ')
print(df[df.isna().any(axis=1)])
print('What are the different types of values in each column?')
print(set(df.dtypes))

