# func_example_001_a_with_its_use.py
# Please refer to func_example_001_without_its_use.py 
#
# Use def to create a function 
# 

# Note - This function does not return any value
# Three arguments/parameters are being passed from the calling program to this function 
def printthreelines (firstlinechar, middlelinechar, thirdlinechar):
    print (firstlinechar * 21)
    print (" " * 10 + middlelinechar + " " * 10 )
    print (thirdlinechar * 21)
 
printthreelines("#", "X", "#")

printthreelines("X", "X", "X")




