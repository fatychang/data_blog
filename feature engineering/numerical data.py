# import the pandas
import pandas as pd

# load the dataset
data = pd.read_csv('restaurant.csv')

# create a new column and set to zero
data['binary_violation'] = 0

data.loc[data['num_of_violations'] > 0, 'binary_violation'] =1
