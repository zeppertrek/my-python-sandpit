# Illustrate duck typing over here
# Class Methods
# Static methods 
# Inheritance
# Dictionary 
# understand concept of immutability

class ListOfValues(object):
    def __init__(self, *args, **kwargs):
        #args -- tuple of anonymous arguments
        #kwargs -- dictionary of named arguments
        print ("In __init__")
        for sName in args:
            print ("Inside the First for loop ")
            print (sName)
        
        for key, value in kwargs.items():
            print ("Inside the second for loop ")
            print("Key and Value  {} --- {}".format (key,value))
			
    def addValue (self, code, value):
	    pass 
		
    