# oops_in_py_example_006.py 

# This won't work, so what are the workarounds ?

# The program looks nice, but will break at run time.  Think about how you will solve this problem. 

class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    #Concept of overloaded constructors  in Python ?
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed 
        self.tricks = []    # creates a new empty list for each dog


    def add_trick(self, trick):
        self.tricks.append(trick)
		
def main():
    d = Dog('Fido')
    e = Dog('Buddy')

    f = Dog('Fido', 'Doberman')
    g = Dog('Buddy', 'Pug')


    d.add_trick('roll over')
    e.add_trick('play dead')
    print ("It is a dog's day")
    print (f.breed)
    print (g.breed)

main()