#try_except_example_001.py
a  = 100
b  = 1

x1 = "a"
x2 = "b"
try:
    c = a / b
    x2 = 1
    print ( x1+x2)
	
	
except ZeroDivisionError as error:
    print(error)
    print ("Division by zero error occurred. Please check your values")
except TypeError as error:
    print(error)
    print ("int and str cannot be concatenated directly")
else:
    print ("In the else clause")
finally:
    print('Cleaning up, irrespective of any exceptions.')