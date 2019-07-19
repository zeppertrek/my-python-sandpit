# func_with_real_decorators_006.py

# This contains logic that actually uses decorators 
# func_with_decorators_001.py , func_with_decorators_002.py, func_with_decorators_003.py, func_with_decorators_004.py, func_with_decorators_005.py 
# These 5 programs play around with functions.  Go through these programs to understand the basics 

# Basic Syntax 
#
# 
#i_need_to_be_decorated = THE_DECORATOR(i_need_to_be_decorated)
#

from functools import wraps

def add_log_info(func):
    @wraps(func)
    def log_info(*args, **kwargs):
        print ("This is pure logging stuff ")
        func(*args, **kwargs)
    return log_info
	

def add_trace_info(func):
    @wraps(func)
    def trace_info(*args, **kwargs):
        print ("This is pure tracing stuff")
        func(*args, **kwargs)
    return trace_info

# Multiple decorators on the same function 

# In what sequence do the decorators execute - top to down or down to top 
# In the example below, how many times does "I am being executed " get printed ?.  Why does it get printed once only ?. 
# 
@add_log_info     ( log_level = 1 )
@add_trace_info   ( trace_level = 100) 
def execute_me(*args, **kwargs):
    list1 = args
    for x in args:
        print (x)
    for w,z in kwargs.items():
        print (w,z)


	
#@add_trace_info 
#@add_log_info
#def ignore_me():
#    print ("I am being ignored ")

aList = [1,2,3,4,5]
aDict = {"Name": "maxy", "Age":24, "Gender": "F", "Active" : "Y"}	
execute_me(*aList, **aDict)
#ignore_me()

#########33333
#
#
#  execute_me = add_trace_info ( add_log_info (execute_me (*args, **kwargs))

