#range_example_001.py
#range converted to lists
#

for i in range(5):
    print(i)
""" 
range([start,] stop [, step]) -> range object
PARAMETER	DESCRIPTION
start	(optional) Starting point of the sequence. It defaults to 0.
stop	(required) Endpoint of the sequence. This item will not be included in the sequence.
step	(optional) Step size of the sequence. It defaults to 1.
"""
	
	
print ("List range(10) ---", list(range(10)))

print ("List range(1,11) ---", list(range(1, 11)))

print ("List range(0,30,5) --- ", list(range(0, 30, 5)))

print ("list(range(0, 10, 3)) ---", list(range(0, 10, 3)))

print ("list(range(0, -10, -1)) ---" , list(range(0, -10, -1)))

print ("list(range(0)) ---", list(range(0)))

print ("list(range(1, 0)) ---", list(range(1, 0)))
