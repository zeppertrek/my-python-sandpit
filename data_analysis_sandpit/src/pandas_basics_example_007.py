#pandas_basics_example_007.py 

import pandas as pd 

names_data1 = {'Name': ["Pi", "Zott", "Plot", "Ki"], 'Age' : [24, 13, 53, 33]}
df = pd.DataFrame (names_data1)

print (df)

df1 = df[df.Age > 30]
print (df1)

names_data2 = {'Name': ["Pi", "Zott", "Plot", "Ki"], 'Age' : [24, 13, 53, 33]}
df = pd.DataFrame (names_data2)

df2 = df[df['Name'].isin (["Pi", "Zott"])]

print (df2)

