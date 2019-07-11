#func_with_decorators_003.py
# This contains logic that lays the groundwork for function and class decorators 


def func1():
    print ([1,2,3,4,5,6])

def func2():
    for x in 'aeiou':
        print (x)

    
def multi_func(input_func):
    print ("Actual name of input_func passed to multi_func is ", input_func.__name__)
    input_func()
          
multi_func(func1)

multi_func(func2)
