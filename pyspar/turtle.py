'''Function definition and invocation examples.'''
#
# Sub routines
#

# Avoid definining these kind of global constants

import DogClass 

APPLICATION_NAME="SPAR-TACUS"

def double(n):
    return 2 * n # Return twice the given number

def printYY():
    print ("YY")
	
def printPP (firstname, middlename, lastname):
    print( '{} --- {} --- {}'.format(firstname, middlename, lastname))

def printGAN():
    print (	APPLICATION_NAME )
	
# The main program
# Call the function with the value 3 and print its result
# Good practice to use main()
def main():
    x = double(3)
    print(x)
    printYY()
    printPP('Sanjiv', 'Mutthana', 'Nagraj')
    printGAN()
	
    pug = DogClass.Dog("pug")
    print (pug.kind)
	
    d = DogClass.Dog("Fido")
    e = DogClass.Dog("Buddy")
    d.add_trick("roll over")
    e.add_trick ("play dead")
    print (d.tricks)
    print (e.tricks)

main()

