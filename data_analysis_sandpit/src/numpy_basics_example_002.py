#numpy_basics_example_002.py
import numpy as np 

# creating arrays
# Just definitions 
# Creating an integer array 1 by 10 filled with zeroes
ar1 = np.zeros(10, dtype='int')
print (ar1)

# Creating a float array with zeroes, 1 by 5
ar2 = np.zeros(5, dtype='float')
print (ar2)

#creating a 2 row x 6 column matrix
ar3 = np.ones((2,6), dtype=float)
print (ar3)

ar3[1,1] = 12345

print (ar3)

