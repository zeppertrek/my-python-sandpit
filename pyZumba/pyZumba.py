#pyZumba main script

import pyZumba.spaceship  

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

	
main()
