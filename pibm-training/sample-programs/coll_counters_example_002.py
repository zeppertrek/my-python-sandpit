#coll_counters_example_002.py

# A Counter is a dict subclass for counting hashable objects. 
# It is a collection where elements are stored as dictionary keys 
# and their counts are stored as dictionary values. 
# Counts are allowed to be any integer value including zero or negative counts. 

import collections 
uniquewords = collections.Counter()
# populates the counter from the list 
for word in ['and', 'then', 'out', 'of', 'the', 'blue','blue', 'birds', 'then', 'flew', 'out']:
    uniquewords[word] += 1
print (uniquewords)

# Create a counter from a String which is an iterable
tmpcnt1 = collections.Counter('Anarchy')
print (tmpcnt1)   

# Create a counter from a String which is an iterable
tmpcnt2 = collections.Counter(['Tea', 'Coffee', 'Whiskey', 'Rum'])
print (tmpcnt2)   

