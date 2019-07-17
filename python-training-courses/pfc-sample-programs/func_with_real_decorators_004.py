# func_with_real_decorators_004.py

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
    def log_info():
        print ("This is pure logging stuff ")
        func()
    return log_info
	

def add_trace_info(func):
    @wraps(func)
    def trace_info():
        print ("This is pure tracing stuff")
        func()
    return trace_info

# Multiple decorators on the same function 

# In what sequence do the decorators execute - top to down or down to top 
# In the example below, how many times does "I am being executed " get printed ?.  Why does it get printed once only ?. 
# 
@add_log_info
@add_trace_info 
def execute_me():
    print ("I am being executed ")

	
@add_trace_info 
@add_log_info
def ignore_me():
    print ("I am being ignored ")
	

execute_me()
ignore_me()



