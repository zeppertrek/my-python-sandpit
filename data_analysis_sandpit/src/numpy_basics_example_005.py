#numpy_basics_example_005.py
# creating np arrays using concatenation 
import numpy as np

# Concatenating 2 or more arrays at once.
x1 = np.array([1, 2, 3])
x2 = np.array([-1, -1, -1])
x3 = np.array([0, 0, 0])
x4 = np.array([2000002, 300002, 4000004])


zzz = np.concatenate([x1, x2,x3, x4])
print (zzz)


#You can also use this function to create 2-dimensional arrays.
temp1 = np.array([[1,2,3,4,5],[4,5,6,7,8]])
zzz = np.concatenate([temp1,temp1])
print (zzz)