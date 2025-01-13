# import pandasm matplot, and seaborn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas import pivot

# load our csv file
df = pd.read_csv('CSV/archivenaturaldisaster/us_disaster_declarations.csv')

# displaying the first few rowa  to get an understanding for the data structure
print(df.head())

#info about dataset
print(df.info())

# checking for msiising values in dataset

print(df.isnull().sum())

# convert date columns to determine easier manipulation
df['declaration_date'] = pd.to_datetime(df['declaration_date'])
df['incident_begin_date'] = pd.to_datetime(df['incident_begin_date'])
df['incident_end_date'] = pd.to_datetime(df['incident_end_date'])

#print the basic statistics
print(df.describe())

#disaster types
disaster_types = df['incident_type'].value_counts()
print(disaster_types)


# frequency of disaster by year
df['year'] = df['declaration_date'].dt.year
disasters_by_year = df['year'].value_counts().sort_index()
plt.figure(figsize=(15,16))
disasters_by_year.plot(kind='bar')
plt.title("Number of Disasters by Year")
plt.xlabel('Year')
plt.ylabel('Number of Disasters')
plt.show()

# most affected by the disasters
states_affected = df['state'].value_counts()
plt.figure(figsize=(15,6))
states_affected.plot(kind='bar')
plt.title("Number of Disasters by State")
plt.xlabel('State')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.show()

# disaater types and their duration
df['duration'] = (df['incident_end_date'] - df['incident_begin_date']).dt.days
sns.boxplot(x='incident_type', y='duration', data=df)
plt.xticks(rotation=90)
plt.title('Duration of Disasters by Type')
plt.xlabel('Disaster Types')
plt.ylabel('Duration (Days)')
plt.show()

# disaster heat map
pivot_table = pd.pivot_table(df, values='declaration_number', index='state', columns='incident_type', aggfunc='count', fill_value=0)
plt.figure(figsize=(20, 10))
sns.heatmap(pivot_table, annot=False, cmap='YlOrRd')
plt.title('Disaster Type by State')
plt.xlabel('Disaster Type')
plt.ylabel('State')
plt.show()
