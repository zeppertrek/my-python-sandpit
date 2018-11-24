#numpy_example_003.py
import numpy as np 

#creating a matrix with a predefined string value 
ar1 = np.full((4,2), '420')
print (ar1)

#creating a matrix with a predefined numeric value 
ar2 = np.full((9,3), 911)
print (ar2)

#create an array with a set of value generated using range 
ar3 = np.arange(0, 30, 3)
print (ar3)

#create an array of evenly spaced elements within a range 
ar4 = np.linspace(10, 100, 10)
print (ar4)

