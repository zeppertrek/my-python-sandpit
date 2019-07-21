# func_with_real_decorators_008.py

# This contains logic that actually uses decorators 
# func_with_decorators_001.py , func_with_decorators_002.py, func_with_decorators_003.py, func_with_decorators_004.py, func_with_decorators_005.py 
# These 5 programs play around with functions.  Go through these programs to understand the basics 

# Basic Syntax 
#
# 
#i_need_to_be_decorated = THE_DECORATOR(i_need_to_be_decorated)
#

from functools import wraps

#
#
#def add_trace_info(func):
#    @wraps(func)
#    def trace_info():
#        print ("This is pure tracing stuff")
#        // Instead of executing func(), we have return func 
#        func()
#    return trace_info
#
#
# @add_trace_info 
# def execute_me():
#    print ("I am being executed ")
#
#
# @decorator1 ( arg1 = value1, arg2 = value 2, ......)
# @decorator2 ( arg1 = value1, arg2 = value 2, ......) 
# func_to_be_decorated_1 ()
#
# @decorator1 ( arg1 = value1, arg2 = value 2, ......)
# @decorator2 ( arg1 = value1, arg2 = value 2, ......) 
# func_to_be_decorated_2 (*args)
#
# @decorator1 ( arg1 = value1, arg2 = value 2, ......)
# @decorator2 ( arg1 = value1, arg2 = value 2, ......) 
# func_to_be_decorated_1 (*args, **kwargs)
#