#tuple_example_003.py

# Weird declarations of a tuple
# Python lets you do this
# Question is - Does it make sense ?

# Model your tuples on real world data
#
myTuple1 = ([],(),[], "a", 1, 1.6, 444555, "goosebumps", {1,2,3,4})

print (myTuple1)

x = 100

myTuple2 = ("aaabbbbbbbbcccccccccccc", type(myTuple1), id(myTuple1), x + 1, print, [[[[[]]]]], {})

print (myTuple2)

myTuple3 = (1,2,3,4,5,6,7)
print (myTuple3)


#myTuple3[0] = 9 ;

print ( "Length / Size of the tuple - 3 is " , len (myTuple3))

myTuple4 = myTuple3[:]
print (myTuple4)




