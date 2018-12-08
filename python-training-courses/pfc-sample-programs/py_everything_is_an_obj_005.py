#py_everything_is_an_obj_005.py

a = 1
b = 1
# 
print(id(a))
print(id(b))
#
# id() returns the actual memory location where the variable is stored. 
# Since id(a) = id(b), we know that a and b both point to a single variable, 
# that resides in a single memory location. 
# This is what we mean by “multiple names bound to single object
print("Result of a is b", a is b)

a = a + 1

c = a 
print ("a = ", a, "b = ", b, "c = ", c)

print("Result of a is c", a is c)

print(id(a))
print(id(c))

print("Result of a is b again", a is b)
