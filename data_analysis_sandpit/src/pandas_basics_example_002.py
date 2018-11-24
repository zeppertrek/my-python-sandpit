#pandas_example_002.py 

import matplotlib.pyplot as plt
import pandas as pd 
#import matplotlib


dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98],
	   "GDP" : [234567, 3456, 897, 97865, 33333]}

#Creating a data frame from a dictionary 
df = pd.DataFrame(dict)
print(df)

#Creating a BAR graph
df.plot(kind='bar',x='country',y='area')
plt.show()

 