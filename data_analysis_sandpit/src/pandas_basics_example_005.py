#pandas_basics_example_005.py 
#create a data frame - 
# dictionary is used here where keys get converted to 
# column names and values to row values.
import pandas as pd 
data = pd.DataFrame({'Country': ['Russia','Colombia','Chile','Equador','Nigeria'],
                     'Rank':[121,40,100,130,11]})
					 
print (data)
print (data.describe())
print (data.info())
# 
print (data.head(2))
print (data.tail(3))
