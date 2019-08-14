# func_with_real_decorators_007.py

# This contains logic that actually uses decorators 
# func_with_decorators_001.py , func_with_decorators_002.py, func_with_decorators_003.py, func_with_decorators_004.py, func_with_decorators_005.py 
# These 5 programs play around with functions.  Go through these programs to understand the basics 

# Basic Syntax 
#
# 
#i_need_to_be_decorated = THE_DECORATOR(i_need_to_be_decorated)
#



# PythonDecorators/decorator_function_with_arguments.py
#
#  Need to understand this example 
# 
def decorator_function_with_arguments(arg1, arg2, arg3):
    def wrap(f):
        print("Inside wrap()")
        def wrapped_f(*args):
            print("Inside wrapped_f()")
            print("These are the Decorator arguments - 3 of them :", arg1, arg2, arg3)
            f(*args)
            print("After f(*args)")
        return wrapped_f
    return wrap

# Can decorator argument values be dynamic ? 
@decorator_function_with_arguments("Deco-rum", "Deco-rate", -99999)
def sayHello(a1, a2, a3, a4):
    print('sayHello arguments - 4 of them :', a1, a2, a3, a4)

#print("After decoration")

print("Calling sayHello() for the first time")
sayHello("say", "hello", "by ", "Lionel Richie")
print("Calling sayHello() for the SECOND time")
sayHello("The", "Police", "Synchronicity", "Great Album")
#
print ("############################################################")
print("Dun dunna done")


##################################################################################3

# Understand how this works 
# 
def decorator_factory(enter_message, exit_message):
    # We're going to return this decorator
    def simple_decorator(f):
        def wrapper():
            print enter_message
            f()
            print exit_message

        return wrapper

    return simple_decorator

@decorator_factory("Start", "End")
def hello():
    print "Hello World"

hello()

#####################################################################################3
#####################################################################################
#
#
#
#  The decorator has arguments 
#
#  The function to be decorated may or may not have arguments .  How is this case handled ?. 
#
#






