#LAMBDAS_example_003.py

# The filter() function in Python takes in a function and a list as arguments. 
# This offers an elegant way to filter out all the elements of a sequence “sequence”, for which the function returns True. 
# Here is a small program that returns the odd numbers from an input list:

# Python code to illustrate 
# filter() with lambda() 
li1= [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 
final_list = list(filter(lambda x: (x%2 != 0) , li1)) 
print(final_list) 




li2= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
      'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
      's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 
final_list2 = list(filter(lambda x: (x in 'aeiou') , li2)) 
print(final_list2) 