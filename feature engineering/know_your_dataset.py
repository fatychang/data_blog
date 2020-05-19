import pandas as pd

# load the dataset
data = pd.read_csv('iris.csv')

# print the first 5 rows of the data
print(data.head())

# print the basic information of the dataset
# including the column name, type of columns, the counts of non-null value etc.
print(data.info())

# print the descriptive statistics of the dataset
print(data.describe())

# print only the column name
print(data.columns)

# use one-hot encoding on the 'variety' column and add a prefix to the new columns
data_onehot = pd.get_dummies(data, columns=['variety'], prefix='C')

# use dummy encoding on the 'variety' column and add a prefix to the new columns
# set the drop_first argument to true
data_dummy = pd.get_dummies(data, columns=['variety'], drop_first=True, prefix='C')


# count the number rows under each category
counts = data['variety'].value_counts()

# create a mask to identify the rows that you want to exclude
mask = data['variety'].isin(counts[counts < 49].index)
data['variety'][mask] = 'Others'
