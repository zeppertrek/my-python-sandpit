# LAMBDAS_example_002.py 
# more on lambdas 
# Python provides several functions which enable a functional approach to programming. 
# map(function_object, iterable1, iterable2,...)
# map functions expects a function object and any number of iterables like list, dictionary, etc. 
# It executes the function_object for each element in the sequence and returns a list of the elements modified by the function object.


# Map, Filter, Reduce - These are very useful functions 

from functools import reduce

def mapFuncs():
    myList = [1, 2, 3, 4]
    result = map(lambda x : x*2, myList) 
	#Output [2, 4, 6, 8]
    print (list(result))
	
	
    myNum1 = [1, 2, 3, 4, 2000]
    myNum2 = [5, 6, 7, 8]
	
    result = map(lambda x,y : x+y, myNum1, myNum2) 
	
    print (list(result))
	    

def filterFuncs():
    number_list = range(-5, 5)
    less_than_zero = list(filter(lambda x: x < 0, number_list))
    print(less_than_zero)

def reduceFuncs():
    product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
    print (product)

	
def main():
    mapFuncs()
    filterFuncs()
    reduceFuncs()
	
	

main()





