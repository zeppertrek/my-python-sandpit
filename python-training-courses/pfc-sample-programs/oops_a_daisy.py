# oopsadaisy.py
#
# Design your classes (blueprints)
# Note - The term used is "Design". As a developer, spend time in designing your classes properly.
#
# Objects/instances are created as per the class blueprint
#
# Understand differences between class and instance attributes
#
# __init__ and __str__  two widely used (dunder) methods
#
# The "self" parameter
#
# Defining additional class and instance methods
#
# Dynamic instance attributes
#
# In this program, a class is progressively enhanced to demonstrate the basic OOP concepts in Python
# 

## The simplest possible class

# This class doesn't really do too much
# Level 1
class Reallysimplesimon1:
    pass

firstguy = Reallysimplesimon1() ;


#Level 2
class Simplesimon2:

    # Question that one should ask - What is the self parameter ?
    #
    # (dunder) method
    # __init__ is used to initialize the object.
    # self represents the instance of the class
    def __init__(self, name, age, gender, birthplace):
        # Note the indentation
        # These are all attributes / instance variables of the object
        self.name = name
        self.age = age
        self.gender = gender
        self.birthplace = birthplace

secondchap = Simplesimon2("Sanjiv", "50", "M", "Pune")

# Level 3
class Simplesimon3:
    # Note this indentation
    # This is a class attribute and not tied to any specific instance/object
    # Be aware of the differences between class and instance attributes
    species = "human"

    def __init__(self, name, age, gender, birthplace):
        # Note the indentation
        # These are all attributes / instance variables of the object
        self.name = name
        self.age = age
        self.gender = gender
        self.birthplace = birthplace

guy01 = Simplesimon3("Sanjiv", "50", "M", "Pune")
guy02 = Simplesimon3("Kapil", "50", "M", "Pune")

# Printing the class attribute
print (Simplesimon3.species)

# Printing the class attribute
print (guy02.name)


# Level 4
class Simplesimon4:
    # Note this indentation
    # This is a class attribute and not tied to any specific instance/object
    # Be aware of the difference between class and instance attributes
    species = "human"

    def __init__(self, name, age, gender, birthplace):
        # Note the indentation
        # These are all attributes / instance variables of the object
        self.name = name
        self.age = age
        self.gender = gender
        self.birthplace = birthplace

    # Instance method
    def printattributes (self):
        print ("Name - {}, Age - {}, Gender - {}, Birthplace - {}".format ( self.name, self.age, self.gender, self.birthplace))

    # __ - dunder method
    def __str__(self):
        return "Name - {}, Age - {}, Gender - {}, Birthplace - {}".format ( self.name, self.age, self.gender, self.birthplace)

guy04 = Simplesimon4("Mutlu", "20", "M", "Pune")

guy04.printattributes()
print (guy04)


guy104 = Simplesimon4("mocha", "40", "F", "Mumbai")
#
# What does this mean ?.  Another instance attribute is being specified at run time
guy104.profession  = "Engineer"

guy104.printattributes()

# What makes this possible.  Hint - It is a dunder method defined somewhere.
print (guy104)

# Check the output
print(guy104.__dir__())

# Check the output
print("__dict__  {}".format (guy104.__dict__))

# Check the output
print("__repr__  {}".format( guy104.__repr__))

# Check the output
print("__hash__  {}".format (guy104.__hash__))


####################################################################
# Level 5
class Simplesimon5:
    # Note this indentation
    # This is a class attribute and not tied to any specific instance/object
    # Be aware of the difference between class and instance attributes
    species = "human"
    genus = "mammalia"
    def __init__(self, name, age, gender, birthplace):
        # Note the indentation
        # These are all attributes / instance variables of the object
        self.name = name
        self.age = age
        self.gender = gender
        self.birthplace = birthplace

    # Instance method
    def printattributes (self):
        print ("Name - {}, Age - {}, Gender - {}, Birthplace - {}".format ( self.name, self.age, self.gender, self.birthplace))

    # __ - dunder method
    def __str__(self):
        return "Name - {}, Age - {}, Gender - {}, Birthplace - {}".format ( self.name, self.age, self.gender, self.birthplace)

    # Class attributes can be referenced through the instance itself
    def printclassattributes(self):
        print ("{} ----- {}".format (self.genus, self.species ))


guy105 = Simplesimon5("Loki", "2", "M", "Pune")

guy105.printclassattributes()

# Referencing the class attributes directly
print (Simplesimon5.species)