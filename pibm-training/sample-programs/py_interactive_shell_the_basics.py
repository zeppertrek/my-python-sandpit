# py_interactive_shell_the_basics.py
# This is not meant to be run as a Python program / module
# Helps to understand / use the Interactive Shell 
# run python to launch the interactive shell 

# The interactive shell really encourages you to be creative
# Run any kind of statement without repercussion :-)

# import this
# displays some interesting stuff about Python 
>>> import this 

>>> help()

help>modules

help> CTRL + C 

help> keywords

# To go back to the >>> prompt 

>>> print ("hi there, just checking out the Python interactive shell")

# using the shell as a calculator 
>>> (10+5) * 20

# This is actually equivalent to <> + ......
>>> "<>" * 8


>>> myList = {1,2,3,4,5,6}
>>> for i in myList:
...     print(i)
...


>>> var1 = [0, 1, 2]
>>> var2=var1
>>> print (var2)
[0, 1, 2]
>>> var1 += [3]
>>> print (var2)
[0, 1, 2, 3]
>>> print (var1)
[0, 1, 2, 3]

>>> x = 1
>>> id(x)

>>> type(x)


>>> exit()


>>> 1 + '2'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> str(1) + '2'
'12'
>>>

>>> '{0} ----- {1} -------{2}'.format ("a", "b", "c")


######################################################################################
>>> a = []
>>> a.append(a)
>>> a