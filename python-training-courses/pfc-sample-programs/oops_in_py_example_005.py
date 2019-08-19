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
		

#############################################################################

class Cat:

    def __init__ (self):
        print ('Initializing the cat instance')

    def instcat(self):
        print ( 'instance method [instcat] called', self)

    @classmethod
    def classycat(cls):
        print ( 'class method [classycat]called', cls)

    @staticmethod
    def staticmethodcat():
        print ( 'static method [staticmethodcat] called')

    def __call__ (self):
        print ("Inside the __call__ method")

##############################################################################		


		
def main():
    d = Dog('Fido')
    e = Dog('Buddy')
    d.add_trick('roll over')
    e.add_trick('play dead')
    print ("It is a dog's day")
    print (d.tricks)
    print (e.tricks)
    #
    #
    # What is happening over here ? 	
    pepper = Cat()
    pepper.instcat()
    pepper.classycat()
    # Note a static method is being invoked using the instance and not the class !!
    pepper.staticmethodcat()
    # Because the class has a __call__ method, we can use it like a function
    pepper()

if __name__== "__main__":
    main()