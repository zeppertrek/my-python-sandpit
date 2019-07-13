#func_with_decorators_004.py

# This contains logic that lays the groundwork for function and class decorators 
# func_with_decorators_001.py , func_with_decorators_002.py, func_with_decorators_003.py, func_with_decorators_004.py, func_with_decorators_005.py 
# These 5 programs play around with functions.  Some examples can be really weird 


def func1():
    print ([1,2,3,4,5,6])

def func2():
    for x in 'aeiou':
        print (x)

def func3():
    z = "x" + "y" + "z"
    print (z)
    print ("***************")

    
x = func1 
y = func2 
z = func3

print (x)
print (y)
print (z)

print (x.__name__)

# This wont work, oviously 
#print (x + y + z)

#Invoking x which is actually a function 
x()

# Both will have the same ID 
print (" ID of func1 and x - ", id (func1), id(x))