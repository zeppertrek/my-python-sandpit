# func_example_003_module.py
# This module contains re-usable functions 
# 

def area_of_rectangle (l,b):
    return l*b

def perimeter_of_rectange (l,b):
    return 2*l+2*b
	

def area_and_perimeter (l,b):
   # return multiple values as a tuple
   # 
   return ( l*b, 2*l+2*b)


def fencing_cost (l:int, b:int, cost:int) ->tuple:
    return ( 2*l+2*b, (2*l+2*b)*cost)

math.sqrt(x)


