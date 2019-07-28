#func_with_decorators_003.py

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

    
def multi_func(input_func):
    print ("Actual name of input_func passed to multi_func is ", input_func.__name__)
    input_func()
          
multi_func(func1)

multi_func(func2)

multi_func(func3)


############################################################################################
