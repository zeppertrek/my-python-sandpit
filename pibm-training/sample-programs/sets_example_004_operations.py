#sets_example_004_operations.py

dataScientist = set(['Python', 'R', 'SQL', 'Git', 'Tableau', 'SAS'])
dataEngineer = set(['Python', 'Java', 'Scala', 'Git', 'SQL', 'Hadoop'])

print (dataScientist.union(dataEngineer))

print (dataScientist.intersection(dataEngineer))

graphicDesigner = {'Illustrator', 'InDesign', 'Photoshop'}

# These sets have elements in common so it would return False
print (dataScientist.isdisjoint(dataEngineer))

# These sets have no elements in common so it would return True
print (dataScientist.isdisjoint(graphicDesigner))

# set of all values of dataScientist that are not values of dataEngineer
print (dataScientist.difference(dataEngineer))

possibleSkills = {'Python', 'R', 'SQL', 'Git', 'Tableau', 'SAS'}
mySkills = {'Python', 'R'}
mySkills.issubset(possibleSkills)