#numpy_example_001.py

# declaring numpy arrays 

import numpy as np

#An array object represents a multidimensional, 
# homogeneous array/container of fixed-size items. 
npa1 = np.array([1,2,3,4,5]) 
print (npa1) 

npa2 = np.array([[1, 2], [3, 4]]) 
print (npa2)

# Not allowed in numpy 
npa3 = np.array([[1, 2,3,4], [3, 4], [1,1,1,1,1]]) 
print (npa3)

npa4 = np.array([[1, 2,3,4], [3, 4,0,1], [1,1,1,1]]) 
print (npa4)

