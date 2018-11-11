# func_example_003_b_uses_a_module.py
# This module contains re-usable functions 
# 

# IMPORTS a module and gives it another name (alias)
import func_example_003_main_module as mymain

print ("Area of the rectangle using imported module is ", mymain.area_of_rectangle (100,20))

print ("Fencing cost using imported module is ", mymain.fencing_cost (100,20, 250))