# spaceship.py

# Every class is implicitly derived from object 
class spaceship (object):
    #totalFleetSize = 100         # example of a class variable shared by all instances
    launchcount = 0
    def __init__(self, spaceshipName, commander, starfleet, missionCode, missionStatus):
        self.spaceshipName = spaceshipName    # instance variable unique to each instance
        self.commander = commander 
        self.starfleet = starfleet 
        self.missionCode = missionCode 	
        self.missionStatus = missionStatus 
        
    @classmethod
    def launch(self, launchStatus):
        self.missionStatus = launchStatus 	
		
    @staticmethod
    def incrLaunchCount():
	    spaceship.launchcount = spaceship.launchcount + 1
	    
