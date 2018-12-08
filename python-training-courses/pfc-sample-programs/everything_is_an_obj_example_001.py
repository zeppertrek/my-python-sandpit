#
# everything_is_an_obj_example_001.py 

# variables, assignments with mutable types
# 
myList1 = ["Deep Purple", "The Who", "Dire Straits", "CCR"]
myList2 = myList1

print ("myList1 id, type and values- ", id(myList1), "<>", type (myList1), myList1)
print ("myList2 id and  and values - ", id(myList2), "<>", type (myList2), myList2)

# Be very careful about this !!!!!!!!!!!!!!!!!!. Remember this.
#myList1 = myList1 + ["Led Zeppelin"]
# We are not using a = a + x, but a += x 
myList1 += ["Led Zeppelin"]

print ("----------------------------------")
print ("myList1 id, type and values- ", id(myList1), "<>", type (myList1), myList1)
print ("myList2 id and  and values - ", id(myList2), "<>", type (myList2), myList2)
 

# myList1 = myList1 + ["Iron Maiden"]
myList1 += ["Iron Maiden"]

print ("----------------------------------")
print ("myList1 id, type and values- ", id(myList1), "<>", type (myList1), myList1)
print ("myList2 id and  and values - ", id(myList2), "<>", type (myList2), myList2)
 