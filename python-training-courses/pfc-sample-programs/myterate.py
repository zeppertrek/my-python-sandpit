# Writing your own iterator
# Re-visit Python's for loop to appreciate the magic of iteration !

# Key concepts
#
# An iterable is anything you’re able to loop over.
# An iterator is the object that does the actual iterating.
# You can get an iterator from any iterable by calling the built-in iter function on the iterable.

import random

# This is an iterable
class Team2:

    """Iterator that counts upward forever."""

    def __init__(self, start):
        self.num = start

    def __iter__(self):
        return self

    def __next__(self):
        num = self.num
        self.num += 1
        return num


myteam = Team2(100)

# iter
# This is an iterator
myiter = iter(myteam)

#
print (" type(myiter) - {}".format(myiter))
#
# using next to iterate over the iterable
print ( "myiter.__next__()  - {}".format(myiter.__next__()))
print ( myiter.__next__())
print ( myiter.__next__())
print ( "next (myiter)  - {}".format(next(myiter)))

class Teamster:

    """Iterator that iterates over a range"""

    def __init__(self, intervalstart, intervalend):
        self.begin = intervalstart-1
        self.end   = intervalend

    def __iter__(self):
        return self

    def __next__(self):
        self.begin += 1
        pointer = self.begin
        if self.begin > self.end:
            raise StopIteration
        else:
            return pointer

myteamster = Teamster(1,20)

# Python's for loop works like magic over any iterable
for i in myteamster:
    print (i)


# Concept of a generator with the yield statement
def get_random_number():
    randomint1 =  random.randint(100, 200)
    randomint2 =  random.randint(100, 200)
    randomint3 =  random.randint(100, 200)
    randomint4 =  random.randint(100, 200)
    randomint5 =  random.randint(100, 200)
    #
    #print ("Random number generated - {}".format(randomint))
    yield randomint1
    yield randomint2
    yield randomint3
    yield randomint4
    yield randomint5

# Check the type, it is interesting
myrandomgen = get_random_number()
print (" type of myrandomgen - {}".format (myrandomgen))

# Retrieve the iterator object
iterrand = iter (myrandomgen)

# Python's for loop once again works like magic over any iterable
for i in iterrand:
        print (i)



