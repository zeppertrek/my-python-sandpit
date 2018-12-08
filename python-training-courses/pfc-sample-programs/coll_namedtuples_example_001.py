#coll_namedtuples_example_001.py
import collections 

Car1 = collections.namedtuple('Car1', ['color', 'mileage'])

S = Car1 ("Red", "100 km")
print (S.color + "---" + S.mileage )
print ("S[0], S[1] format works as well" , S[0], S[1])

# Why are we passing the fields as a string encoding them "color mileage"?
# The answer is that namedtuple’s factory function calls split() on the 
# field names string, so this is really 
Car2 = collections.namedtuple('Car2' , 'color mileage')