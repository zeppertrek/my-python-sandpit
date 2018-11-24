#pandas_basics_example_005.py

#import the pandas library and aliasing as pd
import matplotlib.pyplot as plt
import pandas as pd 
df = pd.DataFrame({'col1': [1,2,3,4], 'col2': [0.1,0.2,0.3,0.4]}, index=['a', 'b', 'c', 'd'])
for row in df.itertuples():
    print(row)