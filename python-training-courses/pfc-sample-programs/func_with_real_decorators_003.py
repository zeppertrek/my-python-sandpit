# func_with_real_decorators_003.py

# This contains logic that actually uses decorators 
# func_with_decorators_001.py , func_with_decorators_002.py, func_with_decorators_003.py, func_with_decorators_004.py, func_with_decorators_005.py 
# These 5 programs play around with functions.  Go through these programs to understand the basics 

# Basic Syntax 
#
# 
#i_need_to_be_decorated = THE_DECORATOR(i_need_to_be_decorated)
#

from functools import wraps

def trignometry_stuff(func):
    @wraps(func)
    def mumbojumbo():
        if func.__name__ == "sinX":
            xname = "SINNNNNNNNNNNNNNN" 
        elif func.__name__ == "cosX":
            xname = "COSSSSSSSSSSSSSSSSSSSSSS"
        elif func.__name__ == "tanX":
            xname = "TTTTTAAAAAAAAAAAAAAAAAAAAAANNNNNNNNNN"
        else:
            xname = "UNKNOWN"
        print (xname)
        # This statement must be noted. The function being decorated will get passed and used over here 
        # 
        func()
    return mumbojumbo
	

@trignometry_stuff  
def sinX():
    print ("Value of sin30 is ", "Sin30")
    # Note the change of name has not taken place  
    # Why ?. What is the difference between 003.py and 002.py 
    print("sinX.__name__ is now ", sinX.__name__)

@trignometry_stuff  
def cosX():
    print ("Value of Cos30 is ", "Cos30")
    print("cosX.__name__ is now ", cosX.__name__)


@trignometry_stuff  
def tanX():
    print ("Value of Tan30 is ", "Tan30")
    print("tanX.__name__ is now ", tanX.__name__)

	
sinX()
cosX()
tanX()



