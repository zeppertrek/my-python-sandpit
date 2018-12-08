#LAMBDAS_example_004.py

# The map() function in Python takes in a function and a list as argument. 
# The function is called with a lambda function and a list and a new list is returned 
# which contains all the lambda modified items returned by that function for each item. Example:

# Python code to illustrate  
# map() with lambda()  
# to get double of a list. 
li1 = [1, 2, 3, 4, 5] 
final_list = list(map(lambda x: x*2 , li1)) 
print(final_list) 


li2 = ["a", "b", "c", "d", "e"] 
final_list2 = list(map(lambda x: x + ">" , li2)) 
print(final_list2) 