#
# everything_is_an_obj_example_002.py 

# Need to figure out mutability with lists WIP WIP
# 
myList1 = ["Deep Purple", "The Who", "Dire Straits", "CCR"]
myList2 = myList1

print ("myList1 id, type and values- ", id(myList1), "<>", type (myList1), myList1)
print ("myList2 id and  and values - ", id(myList2), "<>", type (myList2), myList2)

# Be very careful about this !!!!!!!!!!!!!!!!!!
# We are using a = a + x format 
myList1 =  myList1 + ["Led Zeppelin"]

print ("----------------------------------")
print ("myList1 id, type and values- ", id(myList1), "<>", type (myList1), myList1)
print ("myList2 id and  and values - ", id(myList2), "<>", type (myList2), myList2)
 

myList1 = myList1 + ["Iron Maiden"]


print ("----------------------------------")
print ("myList1 id, type and values- ", id(myList1), "<>", type (myList1), myList1)
print ("myList2 id and  and values - ", id(myList2), "<>", type (myList2), myList2)
 