#arrays_in_py_example_001.py
#
# typecode (must be b, B, u, h, H, i, I, l, L, q, Q, f or d)
#
# Rarely used.  Only numeric values are supported 

import array as arr
a = arr.array("I",[3,6,9])
type(a)

numbers_list = [2, 5, 62, 5, 42, 52, 48, 5]
numbers_array = arr.array('i', numbers_list)

print(numbers_list, "<<<2:5 slice>>>",  numbers_array[2:5]) # 3rd to 5th
print(numbers_list, "<<<slice starting from :-5>>>", numbers_array[:-5]) # beginning to 4th
print(numbers_list, "<<<slice starting from 5:>>>",numbers_array[5:])  # 6th to end
print(numbers_list, "<<<The complete slice starting using >>>",numbers_array[:])   # beginning to end


single_digit_numbers = [0,1,2,3,4,5,6,7,8,9]
sdn_array = arr.array('i', single_digit_numbers)

print(sdn_array, "<<<slice starting from :-2>>>", sdn_array[:-2]) # beginning to 4th
