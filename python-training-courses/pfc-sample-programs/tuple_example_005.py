# tuple_example_005.py
# This URL is interesting http://radar.oreilly.com/2014/10/python-tuples-immutable-but-potentially-changing.html 

bollywood_villians = ('Ranjit', 'Prem Chopra', 'Amjad Khan', 'Shakti Kapoor', 'Pran', 'Amrish Puri')

print ( "id, type and values of bollywood_villians", id (bollywood_villians), type(bollywood_villians), bollywood_villians)

print ("Have assigned (bollywood_villians) to (new_age_villians)" )
new_age_villians = bollywood_villians

print ( "id, type and values of new age villians", id (new_age_villians), type(new_age_villians), new_age_villians)

t_or_f = new_age_villians == bollywood_villians
# Traditional equality i.e. same values 
print ("Is new_age_villians == bollywood_villians  ", t_or_f)

t_or_f = new_age_villians is bollywood_villians
#
# Remember variables.  Do both refer to the same object ? 
print ("Is new_age_villians IS bollywood_villians  ", t_or_f)


bollywood_villians = ('Ranjit', 'Prem Chopra', 'Amjad Khan', 'Shakti Kapoor', 'Pran', 'Amrish Puri', 'Danny Denzongpa', 'Ajit')

print ( "id, type and values of bollywood_villians after a = b", id (bollywood_villians), type(bollywood_villians), bollywood_villians)
print ( "id, type and values of new age villians", id (new_age_villians), type(new_age_villians), new_age_villians)


t_or_f = new_age_villians == bollywood_villians
print ("Is new_age_villians == bollywood_villians  ", t_or_f)

t_or_f = new_age_villians is bollywood_villians
print ("Is new_age_villians IS bollywood_villians  ", t_or_f)



############################################################################
############################################################################

xtc = tuple()
print (xtc)

xtc = tuple('hogwarts castle')
print (xtc)

xtc = ('z', 'e', 'd', 'g', 'e')

print (xtc[0])
 
print (xtc[1:3])
print (sorted (xtc))



