#pandas_series_example_001.py 

#import the pandas library and aliasing as pd
import pandas as pd
import numpy as np

# Initialize a Pandas series 
# One dimensional labelled arrays 
s = pd.Series()
print (s)

#Create a series based upon a numpy array 
data1 = np.array(['axe','bib','cod','die', 'elf', 'foe', 'git', 'hip' ,'sin'])
s = pd.Series(data1)
print (s)


# Dictionary keys are used to construct index
data2 = {1001 : "Ajay", 1002 : "Mohit", 1003: "Axel", 1004 : "Gunner", 1005 : "Freud", 1006 : "BB"}
s = pd.Series(data2)
print (s)


alphaX = pd.Series(["and","but","can","do","every"],index = [1,2,3,4,5])

#retrieve multiple elements
print (alphaX[[1,3,5]])