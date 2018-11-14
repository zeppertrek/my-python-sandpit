#coll_counters_example_001.py
#
# treat counter as a frequency table
# 
import collections 

myCounter = collections.Counter()

print ("Is myCounter a sub class of dictionary : ", issubclass(collections.Counter,dict))

#c=Counter(['a','b','c','a','b','a'])

c1=collections.Counter("qwertyqwertyblinkertyblinktiddlywinks")
print (c1)

c2=collections.Counter([1,11,12,13,12,12,1,1,1,1, "a", "a", "a", (1,2,3), (1,2,3), "pqr"])

print (c2)

# This will not work because some of the entries are lists  
c3=collections.Counter([[1,2,3,4], [1,2,3,4], "a", "b", "a", "b"])
print (c3)
