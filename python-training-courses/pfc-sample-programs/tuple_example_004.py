#tuple_example_004.py
# Using negative indexes
# Packing, unpacking 

bond_actors = ('Sean Connery', 'Roger Moore', 'Pierce Brosnan', 'Daniel Craig')

print ("Printing in reverse order using negative indexes ", bond_actors[-1], bond_actors[-2], bond_actors[-3], bond_actors[-4])

(ba1, ba2, ba3, ba4) = bond_actors

print (ba1, "\n", ba2, "\n", ba3, "\n", ba4)

#another way 

(bar1, bar2, bar3, bar4) = ('Sean Connery', 'Roger Moore', 'Pierce Brosnan', 'Daniel Craig')

print (bar1, "\n", bar2, "\n", bar3, "\n", bar4)