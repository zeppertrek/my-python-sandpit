#try_except_example_003.py

import sys

try:
    f = open('idontexist.txt')
    s = f.readline()
except:
    # Avoid using just the except clause.  
    # This type of exception handling results in programming errors being hidden 
    print("EXCEPT block - Unexpected error:", sys.exc_info()[0])
    # This will trigger the real exception as well 
    raise