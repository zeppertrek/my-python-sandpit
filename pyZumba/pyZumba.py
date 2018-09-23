#pyZumba main script

import pyZumba.spaceship  
#import pyZumba.utils.ListOfValues
from pyZumba.utils import ListOfValues

def kwargsTest(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


def main():
    print ("Inside pyZumba main")
    uss = pyZumba.spaceship.spaceship( "USS-Enterprise", "Captain Kirk", "Outer Reaches", "Top Secret", "Awaiting Clearance")	
    uss.launch ("Launched")
    print (uss.missionStatus)
    pyZumba.spaceship.spaceship.incrLaunchCount()
    print ( pyZumba.spaceship.spaceship.launchcount)
    pyZumba.spaceship.spaceship.incrLaunchCount()
    print ( pyZumba.spaceship.spaceship.launchcount)
    pyZumba.spaceship.spaceship.incrLaunchCount()
    print ( pyZumba.spaceship.spaceship.launchcount)
    #	
    #
	
	# Tuple 
    months = ('January','February','March','April','May','June')
	# List 
    myList = ['Tom', 'Snappy', 'Kitty', 'Jessie', 'Chester']
    phonebook = {'Andrew Parson':8806336, 'Emily Everett':6784346, 'Peter Power':7658344, 'Lewis Lame':1122345}
    #lov = pyZumba.utils.ListOfValues.ListOfValues (*myList, **phonebook )
    lov = ListOfValues.ListOfValues (*myList, **phonebook )

	
main()
