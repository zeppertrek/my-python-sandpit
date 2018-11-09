#tuple_example_002.py
#tuples can be declared in all sorts of ways  
#tuples, though immutable, can store mutable objects 
#declarations can get really weird  

myTuple1=()

print ("Type of myTuple1 and value -- ", type(myTuple1), myTuple1)

myTuple2=(())

print ("Type of myTuple2 and value -- ", type(myTuple2), myTuple2)

myTuple3=((),(),(),())

print ("Type of myTuple3 and value -- ", type(myTuple3), myTuple3)

# Trying to mutate myTuple1=()
print ("Attempting to mutate myTuple1")
# This will work 
myTuple1=("a", "b","c")
print (myTuple1)

# This will work 
myTuple1=("a", "b","c" , 1,2,3,4,5)
print (myTuple1)
#
# This will not work 
myTuple1 = myTuple1 + ("dddd")
print ("myTuple1 is now ", myTuple1)
#
#
