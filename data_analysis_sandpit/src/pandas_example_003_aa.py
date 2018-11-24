#pandas_example_003_aa.py 

import matplotlib.pyplot as plt
import pandas as pd 
import matplotlib 

# Enable inline plotting
# %matplotlib inline

# The inital set of cars  and sales 
mycars = ['BMW','Merc','Honda','Ford','Chrysler', 'VW', 'SAAB']
mysales = [20004, 36789, 12377, 578, 91723, 9002, 7345]

# Creating the data frame and plotting the graph 
df = pd.DataFrame({'cars' : mycars , 'sales' : mysales})
# This is the horizontal bar graph 
df.plot(kind='barh',x='cars',y='sales')
plt.show()
