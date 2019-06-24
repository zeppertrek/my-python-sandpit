# oops_in_py_example_005.py 

class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    # Concept of overloaded constructors  in Python ?
    #def __init__(self, name, breed):
    #    self.name = name
    #    self.breed = breed 
    #    self.tricks = []    # creates a new empty list for each dog


    def add_trick(self, trick):
        self.tricks.append(trick)
		
def main():
    d = Dog('Fido')
    e = Dog('Buddy')
    d.add_trick('roll over')
    e.add_trick('play dead')
    print ("It is a dog's day")
    print (d.tricks)
    print (e.tricks)

if __name__== "__main__":
    main()