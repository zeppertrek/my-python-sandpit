
#only_tuples.py
#Once created

# Simple tuple 
Runners = ( 'Chester', 'Bennington', 'Bill', 'Gates', 'Derulo' )

# Tuple within a tuple...similar to array of arrays....
Relay_Team = ( ("jack", "Jim", "john", "jake"), ('Tom', 'Snappy', 'Kitty', 'Jessie'))

print (Relay_Team[0])
print (Relay_Team[1])
#
print (Relay_Team[0][0])

print (Runners)

# Are we really modifying the tuple ? Aren't tuples meant to be immutable ! ?
Runners = ( 'Chester', 'Bennington', 'Bill', 'Gates', 'Derulo', 'Batman')

print (Runners)

txxx = (1, 2, "a", "delta", 5.7)

print (txxx)