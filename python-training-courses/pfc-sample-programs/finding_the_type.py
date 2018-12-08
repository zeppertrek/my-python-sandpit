#finding_the_type.py

print (type(print))


print = 77

# Really bad programming 
# we used the name print as a variable. In so doing it lost its original behavior as a function to print
# the console. 
# While we can reassign the names print, str, type, etc., it generally is not a good idea to do so.
print ("Will I still continue to work")