#tuple_nesting_example_005.py


# Tuples can contain nested elements 

i_am_a_nested_tuple = ((1,2,3), (4,5,6), (7,8,9))

print ( i_am_a_nested_tuple )

# Real world example
# 
dwarves = ( (1, "Dopey"), (2, "Grumpy") ,(3, "Sneezy"), ( 4, "Bashful"), (5, "doc"), ( 6, "Happy"),( 7, "sleepy"))

print (dwarves) 

# Using the standard for loop to iterate through the tuple
for dwarf in dwarves:
    print (dwarf)
    #
    for xy in dwarf:
        print ( xy )

#
print ("Iterating using the for loop with range(len())")

for  i in range(len(dwarves)):
    print(dwarves[i]) 
    i += 1

# Comprehension
# 
print ("Using List comprehension - Single line statement, amazing isn't it  ")
[print(i) for i in dwarves]


