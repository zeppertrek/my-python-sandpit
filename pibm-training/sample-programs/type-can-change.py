# The type of a variable can change
# ..........
# ..............
# Many programming languages do not allow this

#type-can-change.py


a = 10
print('First, variable a has value', a, 'and type', type(a))
a = 'ABC'
print('Now, variable a has value', a, 'and type', type(a))