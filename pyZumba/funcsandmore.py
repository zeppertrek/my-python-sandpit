#  More about functions in Python 


def whats_on_the_telly(penguin=None):
    if penguin is None:
        penguin = []
    penguin.append("property of the zoo")
    return penguin
	
def whats_on_the_telly2(programs=None):
    if programs is None:
        programs = []
    programs.append("snakes")
    return programs

	
birds = []
reptiles = []

# 
#Default parameter values are evaluated from left to right when the function definition is executed. 
#This means that the expression is evaluated once, when the function is defined, 
#and that the same “pre-computed” value is used for each call. 
#This is especially important to understand when a default parameter is a mutable object, 
#such as a list or a dictionary: if the function modifies the object (e.g. by appending an item to a list), 
#the default value is in effect modified.

# Pass by Value / Pass by Copy ? 

print ( whats_on_the_telly(birds))
print ( whats_on_the_telly(birds))

print (whats_on_the_telly2(reptiles))
print (whats_on_the_telly2(reptiles))

# This prints the ID
print (whats_on_the_telly)

# This too prints the ID 
print (whats_on_the_telly2)
