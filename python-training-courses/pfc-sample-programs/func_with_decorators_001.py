#func_with_decorators_001.py 

# This contains logic that lays the groundwork for function and class decorators 
# func_with_decorators_001.py , func_with_decorators_002.py, func_with_decorators_003.py, func_with_decorators_004.py, func_with_decorators_005.py 
# These 5 programs play around with functions.  Some examples can be really weird 

def concat_two_strings(name1, name2):
    z = name1 + name2
    return f"Hello {z}"

def  useless_func ( name ):
    return f"Useless function is returning {name}"

def pass_a_func(i_am_a_func):
    print ("Real name of i_am_a_func is ", i_am_a_func.__name__)
    return i_am_a_func("Alpha", "Beta")
	
def func_within_funcs_01():
    print ( "XXX1. This is outer function!")
    def inner_function():
        print  ("XXX2. This is inner function, inside outer function!")
    print ("XXX3. This is outside inner function, inside outer function!")
    return inner_function()

def func_within_funcs_02():
    print ( "ZZZ1. This is outer function!")
    def inner_function():
        print  ("ZZZ2. This is inner function, inside outer function!")
    print ("ZZZ3. This is outside inner function, inside outer function!")
    inner_function()

def func_within_funcs_03():
    print ( "QQQ1. This is outer function!")
    def inner_function():
        print  ("QQQ. This is inner function, inside outer function!")
    print ("QQQ. This is outside inner function, inside outer function!")


	
def main():
    # This is significant
    # The argument is a function name - functions are first class objects in Python 
    # It is passing any variable 
    x = pass_a_func( concat_two_strings)
    print (x)
    #
    print ("***********************************************************")
    print ("                                                           ")
    func_caller = func_within_funcs_01()
    #
    print ( "ID, Type and Value of func_caller", id(func_caller), type(func_caller), func_caller)

    print ("***********************************************************")
    print ("                                                           ")
    func_within_funcs_02()

    print ("***********************************************************")
    print ("                                                           ")
 
    func_within_funcs_03()

main()
	