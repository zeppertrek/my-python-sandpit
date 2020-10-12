# decomoreco.py
# The decorators themselves have arguments passed to them
#

#############################################################################################################

import functools

print ("PART 1 ::: Decorators -  Function to be decorated accepts parameters ")
#
#
# @decoratorwithargs (..., ..., ..., ...)
# def func2bdecorated(*args, **kwargs ):
#  .............................
# ..................................
# retval = func2bdecorated(..., ..., ...)
#
# So, this is what happens -
#
# decoratorwithargs = decoratorwithargs ( args1, args2)
# This returns the reference of decorator_wrapper
# Then decorator_wrapper (func2bdecorated) is called.
# Remember because of closures, arg1 and arg2 is remembered
# This returns func_wrapper
# Now, func_wrapper remembers arg1, arg2 and func2bdecorated
#
# finally it is func_wrapper invoked with *args and **kwargs

def  decoratorwithargs (arg1, arg2):
    #
    # The function to be decorated receives its arguments through the wrapper
    # This will preserve information about the original function.

    def decorator_wrapper (myfunc):
        #
        @functools.wraps (myfunc)
        def func_wrapper(  *args, **kwargs):
            #
            print (":::1::: pre statemnt 1 in func_wrapper - {} ".format(myfunc.__name__))
            retval = myfunc(*args, **kwargs)
            print (":::1::: post statemnt 1 in func_wrapper - {} >>> {} ### {}".format (retval, arg1, arg2 ))
            return retval
        return func_wrapper
    print (":::1::: Inside decoratorwithargs - {} and {}".format(arg1, arg2))
    return decorator_wrapper

@decoratorwithargs (arg1 = "TESTARG1", arg2 = "TESTARG2" )
def func2bdecorated(*args, **kwargs ):
    argscount = len(args)
    kwargscount = len(kwargs)
    return argscount + kwargscount

retval = func2bdecorated( *["1", "delta", "gforce"], **{"1":1, "2": 2})

print (":::1::: func2bdecorated return value - {} ".format(retval))