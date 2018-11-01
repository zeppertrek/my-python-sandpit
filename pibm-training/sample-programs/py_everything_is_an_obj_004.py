#py_everything_is_an_obj_004.py

a = "spam"
b = "spam"
# 
print(id(a))
print(id(b))
#
# id() returns the actual memory location where the variable is stored. 
# Since id(a) = id(b), we know that a and b both point to a single variable, 
# that resides in a single memory location. 
# This is what we mean by “multiple names bound to single object
print(a is b)

b = "spam22222222"
print(id(b))
print(a is b)
