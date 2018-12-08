#ltd.py - Lists, Tuples and Dictionaries in Python
# Defining a variable that can be used in this module
# Lists in Python  
# Shallow vs Deep copy
# Generalizing Iterators 
#     >> The concept of iterators/generalized looping is an important one and must be properly understood  


myUserList = ['sanjiv','ananya','rohit','priya','spikey','muttli']
myRolesList =[]

def main():
    #Looping through a List
	#using a for loop
    print ("###################################### Generic Iteration")	
    for users in myUserList:
        print (users)
    print ("###################################### For iteration using an index ")	
    for i in range(len(myUserList)):
        print (myUserList[i])	
    print ("###################################### While ")	

    myUserList[len(myUserList):] = ["puttliXXXX"]		
    j = 0
    while j < len(myUserList):
        myUserList[j]
        print (myUserList[j])
        j += 1

    # Create a shallow copy of the list 		
    myShallowUserList = myUserList[:]


	#Nested List 
    matrix = [ [1,2,3], [4,5,6], [7,8,9] ]
    print (matrix)
	
main()