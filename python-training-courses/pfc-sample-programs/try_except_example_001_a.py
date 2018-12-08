#try_except_example_001_a.py
a  = 100
b  = 1

x1 = "a"
x2 = "b"
try:
    c = a / b
    x2 = 1
    print ( x1+x2)
	
# This is exception that is used to capture any type of error.  
# Use the more specific exception types 
except Exception  as error:
    print(error)
    print ("int and str cannot be concatenated directly")
else:
    print ("In the else clause")
finally:
    print('Cleaning up, irrespective of any exceptions.')