# func_example_003_c_uses_a_module.py
# This module contains re-usable functions 
# 

# IMPORTS specific functions from a module 
#
from func_example_003_main_module import area_of_rectangle, fencing_cost 

print ("Area of the rectangle using imported module is ", area_of_rectangle (100,20))

print ("Fencing cost using imported module is ", fencing_cost (100,20, 250))