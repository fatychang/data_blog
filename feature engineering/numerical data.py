# import the pandas
import pandas as pd

# load the dataset
data = pd.read_csv('restaurant.csv')

# create a new column and set to zero
data['binary_violation'] = 0

data.loc[data['num_of_violations'] > 0, 'binary_violation'] =1


# Bin the numerical data
import numpy as np
data['binned_group'] =pd.cut(data['num_of_violations'],
                        bins=[-np.inf, 0, 2, np.inf], labels=[1, 2, 3]) 
