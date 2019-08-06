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


#########################################################################################
# multiple funcs in a single func 
def functions_within_a_func():
    print ( "ZZZ1. This is outer function!")
    def inner_function_01():
        print  ("ZZZ_01. This is inner function, inside outer function!")
    def inner_function_02():
        print  ("ZZZ_02. This is inner function, inside outer function!")
    def inner_function_03():
        print  ("ZZZ_03. This is inner function, inside outer function!")
    def inner_function_04():
        print  ("ZZZ_04. This is inner function, inside outer function!")
    def inner_function_05():
        print  ("ZZZ_05. This is inner function, inside outer function!")
    print ("ZZZ3. This is outside inner function, inside outer function!")
    inner_function_01()
    inner_function_02()
    inner_function_03()
    inner_function_04()
    inner_function_05()
    
    return [inner_function_01, inner_function_02, inner_function_03, inner_function_04, inner_function_05 ]
###############################################################################################

def wheels_within_wheels():
    print ( "ZZZ1. This is outer function!")
    def inner_function_01():
        print  ("ZZZ_01. This is inner function, inside outer function!")
        def inner_inner_func_01():
            print ("ZZZ_01_ZZZ_01 : This is the inner inner func within - inner_function_01")
        inner_inner_func_01()
        return inner_inner_func_01
    def inner_function_02():
        print  ("ZZZ_02. This is inner function, inside outer function!")
    print ("ZZZ3. This is outside inner function, inside outer function!")
    inner_function_01()
    inner_function_02()
    return [inner_function_01, inner_function_02]



	
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

    # Use of a list to return multiple values, here functions, from a single function 
    fn1, fn2, fn3, fn4, fn5 = functions_within_a_func() 
    print ( "functions_within_a_func()  - Types of fn1, fn2, fn3, fn4, fn5 are ",  type(fn1), type(fn2),type(fn3),type(fn4),type(fn5) ) 
	
    # Use of a list to return multiple values, here functions, from a single function 
    fn1, fn2 = wheels_within_wheels() 
    print ( "wheels_within_wheels() - Types of fn1, fn2 ",  type(fn1), type(fn2) ) 
    print ("name of fn1 is ", fn1.__name__)    
    #fn1.inner_inner_func_01() 	
	
    fn1_inner = fn1()
    fn1_inner()
    print ("name of fn1_inner is ", fn1_inner.__name__)
main()
	