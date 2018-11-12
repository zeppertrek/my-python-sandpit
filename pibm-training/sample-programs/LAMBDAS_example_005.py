#LAMBDAS_example_005.py

# Python code to illustrate  
# reduce() with lambda() 
# to get sum of a list 
from functools import reduce
li1 = [-1, 20, 16, 0, -5, 73] 
sum = reduce((lambda x, y: x + y), li1) 
print (sum) 


li2 = ["a--", "b--", "c--", "d--", "e--", "f--"] 
strcat = reduce((lambda x, y: x + y), li2) 
print (strcat) 