#try_except_example_002.py
a  = 100
b  = 1

x1 = "a"
x2 = "b"
try:
    # Using the raise statement to force a specified exception to occur
    raise NameError('PIBM Testing')
except NameError  as error:
    print(error)
    print ("custom error being raised ")
else:
    print ("In the else clause")
finally:
    print('Cleaning up, irrespective of any exceptions.')