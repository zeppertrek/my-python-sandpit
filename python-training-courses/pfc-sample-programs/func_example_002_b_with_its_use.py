# func_example_002_b_with_its_use.py 
# refer to func_example_002_without_its_use.py 
# WILL NOT WORK 


num01, num02, num03, num04, num05, num06, num07, num08, num09, num10 = 1,2,3,4,5,6,7,8,9,10


# Calculate and Print sum of the first 5 numbers 
sum1 = add_numbers (num01, num02, num03, num04, num05)
print ("Sum of the first 5 numbers is - ", sum1 )


# Calculate and Print sum of the numbers from 6 to 10 
sum2 = add_numbers (num06, num07, num08, num09, num10)
print ("Sum of the numbers from 6 to 10 - ", sum2 )


# Calculate and Print sum of the numbers in odd positions 
sum3 = add_numbers (num01, num03, num05, num07, num09)
print ("Sum of the numbers in odd positions - ", sum3)


# Passing variable number of arguments to the function 
# This program will not work 
# All functions must be defined before any are used. 
# However, the functions can be defined in any order, as long as all are defined before any executable code uses a function.
def add_numbers (*myNumbers):
    sum = 0
    for i in myNumbers:
        sum = sum + i
    return sum 

