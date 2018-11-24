#numpy_example_008.py
import numpy as np 
# A structured array
my_array = np.ones(3, dtype=([('foo', int), ('bar', float)]))
# Print the structured array
print (my_array['foo'])
print (my_array['bar'])

print (my_array)
