# tuple_example_005.py
# 

bollywood_villians = ('Ranjit', 'Prem Chopra', 'Amjad Khan', 'Shakti Kapoor', 'Pran', 'Amrish Puri')

print ( "id, type and values of bollywood_villians", id (bollywood_villians), type(bollywood_villians), bollywood_villians)

print ("Have assigned (bollywood_villians) to (new_age_villians)" )
new_age_villians = bollywood_villians

print ( "id, type and values of new age villians", id (new_age_villians), type(new_age_villians), new_age_villians)

t_or_f = new_age_villians == bollywood_villians
print ("Is new_age_villians == bollywood_villians  ", t_or_f)

t_or_f = new_age_villians is bollywood_villians
print ("Is new_age_villians IS bollywood_villians  ", t_or_f)


bollywood_villians = ('Ranjit', 'Prem Chopra', 'Amjad Khan', 'Shakti Kapoor', 'Pran', 'Amrish Puri', 'Danny Denzongpa', 'Ajit')

print ( "id, type and values of bollywood_villians after a = b", id (bollywood_villians), type(bollywood_villians), bollywood_villians)
print ( "id, type and values of new age villians", id (new_age_villians), type(new_age_villians), new_age_villians)


t_or_f = new_age_villians == bollywood_villians
print ("Is new_age_villians == bollywood_villians  ", t_or_f)

t_or_f = new_age_villians is bollywood_villians
print ("Is new_age_villians IS bollywood_villians  ", t_or_f)
