# func_with_real_decorators_001.py

# This contains logic that actually uses decorators 
# func_with_decorators_001.py , func_with_decorators_002.py, func_with_decorators_003.py, func_with_decorators_004.py, func_with_decorators_005.py 
# These 5 programs play around with functions.  Go through these programs to understand the basics 


# ordinary = make_pretty(ordinary)


def make_pretty(func):
    def inner():
        print("A.make_pretty.inner - I am the decorator ")
        # This statement must be noted. The function being decorated will get passed and used over here 
        # 
        func()
    return inner


# Here is the decoration 
@make_pretty
def ordinary():
    print("ordinary() - B.I am ordinary")
	
def main():
    print ("Calling the ordinary() function which has a decorator called make_pretty")
    ordinary()

main()

################################333

def make_pretty2(funcX):
    def inner2():
        print("A.make_pretty2.inner - I am the decorator ")
        funcX()
    return inner2

def ordinary2():
    print("ordinary2() - B.I am ordinary")

print ("Using standard syntax -----")
ordinary22 = make_pretty2(ordinary2)
ordinary22()

#
# this is pretty much what @make_pretty does above . 
# 
ordinary2 = make_pretty2(ordinary2)
ordinary2()

##########################################################################################3

from functools import wraps

def xxgreeting(func):
    @wraps(func)
    def xxfunction_wrapper(x):
        """ function_wrapper of greeting """
        print("Hi, " + func.__name__ + " returns:")
        # Note here return is used instea of just func(x)
        return func(x)
    return xxfunction_wrapper

@xxgreeting
def  xxmyfunc ( num1):
    return num1 + 1 

print ("Executing xxmyfunc ------")
print ( xxmyfunc (100) )