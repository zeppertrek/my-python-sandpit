#pandas_example_001.py

#import the pandas library and aliasing as pd
import matplotlib.pyplot as plt
import pandas as pd 

#Empty data frame 
df = pd.DataFrame()
print (df)

# Data frame from a simple list 
data = ["clam","cham", "chowder", "prouder", "stouter"]
df = pd.DataFrame(data)
print (df)

# Converting a nested list to a data frame 
data = [['Princeton',155550],['Harvard',11222],['Yale',13000]]
df = pd.DataFrame(data,columns=['University','Students'])
print (df)

df.plot(kind='bar',x='University',y='Students')
plt.show()