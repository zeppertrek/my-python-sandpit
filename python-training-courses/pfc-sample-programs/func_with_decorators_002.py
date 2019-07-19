#func_with_decorators_002.py

# This contains logic that lays the groundwork for function and class decorators 
# func_with_decorators_001.py , func_with_decorators_002.py, func_with_decorators_003.py, func_with_decorators_004.py, func_with_decorators_005.py 
# These 5 programs play around with functions.  Some examples can be really weird 


import math

# This is interesting
# Passing a function as a parameter, just like passing any other variable
# Allows us to have a function that can completely change in behaviour
def foo(func):
    print("The function " + func.__name__ + " was passed to foo")
    res = 0
    for x in [1, 2, 2.5]:
        #func below will get substituted with the actual function name passed to foo
        res += func(x)
    return res

print(foo(math.sin))
print(foo(math.cos))


# at run time, we have added an attribute to a function 
# Remember a function is a first class object !
foo.xcount = 1 
print ( "foo.xcount",1)