##py_everything_is_an_obj_002.py
# Don't worry about what [1,2,3] is.  These are LISTS which we will learn about later. 

a = [1, 2, 3]
b = [1, 2, 3]



print(id(a))

print(id(b))

print(a is b)

print ("In this case, you can see that the objects that a and b point to occupy different places in memory.")
print ("Why did Python behave differently in this example? ")
print ("The difference is that a string is immutable, but a list is mutable.")
print (" The above lines of code created two separate lists")