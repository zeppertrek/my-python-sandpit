# for_loop_example_005_permutations.py
# The first letter varies from A to C
for first in 'ABC':
    # The second varies from A to C
    for second in 'ABC': 
	    # No duplicate letters allowed
        if second != first: 
		    ## The third varies from A to C
            for third in 'ABC': 
                # Don't duplicate first or second letter
                if third != first and third != second:
                    print(first + second + third)