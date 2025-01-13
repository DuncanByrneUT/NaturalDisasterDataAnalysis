# import pandasm matplot, and seaborn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# load our csv file
df = pd.read_csv('CSV/archivenaturaldisaster/us_disaster_declarations.csv')

# displaying the first few rowa  to get an understanding for the data structure
print(df.head())

#info about dataset
print(df.info())

# checking for msiising values in dataset

print(df.isnull().sum())

