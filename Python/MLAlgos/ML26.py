# Rescaling

import pandas as pd
from numpy import set_printoptions
from sklearn.preprocessing import MinMaxScaler

filename = 'indians-diabetes.data.csv'

hnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

df = pd.read_csv(filename, names=hnames)
array = df.values                   # to get only data out of the collected data+metadata

x = array[:, 0:8]                   # [rows , cols]
y = array[:, 8]


scaler = MinMaxScaler(feature_range=(1, 5))         # Transform the data between 1 to 5(included)

# First Method
rescaledx = scaler.fit_transform(x)                 # Transform only input

# Summarize transformed data
set_printoptions(precision=2)
print(rescaledx[: 30, : ] )                         # First 30 rows all columns
