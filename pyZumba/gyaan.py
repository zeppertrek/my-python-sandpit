#gyaan.py

"""
Some Gyaan 
for beginners ...see DocString
"""

# Popular Python module 
import requests

# FYI - Java will not allow this
#So hasn't variable just changed type ?
#The answer is a resounding no. variable isn't an object at all - it's a name. 
#In the first statement we create an integer object with the value 3 and bind the name 'variable' to it. 
#In the second statement we create a new string object with the value hello, and rebind the name 'variable' to it. 
#If there are no other names bound to the first object 
#(or more properly no references to the object - not all references are names)
# then it's reference count will drop to zero and it will be garbage collected.
#
variable = 3
variable = 'hello'

# Global in scope
fname = 'sanjiv'

def myfunc():
    fname = 'myfunc name'
    print ("my func -- " + fname )
	
def myfunc2():
    print ("my func2 -- " + fname )

def radius (diameter):
    # Function within a function . Nesting of functions 
    def innerFunc (n):
        return n/2
    return innerFunc(diameter)
	


print ("gyaan in action")

# Exception handling 
try:
    r = requests.get('https://github.com/timeline.json')
    print (r.text)
except:
    print ("Could not connect to GITHUB")


print ("Global fname -- " + fname )

myfunc()

myfunc2()


a=2
b=3
c=3
# Neat ....
print(f"a={a}, b={b}, c={c}")

# Calling a function directly in the print statement 
print (radius(100))



# Lambda 
# Creating small anonymous functions
# Where is this useful 
# Need to understand this concept 

def make_incrementor(n):
    return lambda xx: xx + n

f = make_incrementor(42)
print (f(0))
print (f(1))


def add_three_numbers(a,b,c):
    return lambda a,b,c: a + b + c

g = add_three_numbers(a,b,c);
# checking the type of g
print (type(g))
print (g(1,2,3))


