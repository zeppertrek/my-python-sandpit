#data_structures_general_stuff_001.py

tastydishes = ['Thai Green Curry', 'Wontons','Risotto', 'Chicken Stroganoff', 'Garlic Bread']
print ("Playing around with lists")
print (tastydishes)
print()
print ("Length of tastydishes is ", len (tastydishes))

print ()
# The slice of s from i to j is defined as the sequence of 
# items with index k such that i <= k < j
print ("Slice [2:3] of tastydishes is  ", tastydishes[2:3])

if 'veg lazeez' in tastydishes:
    print ("Veg lazeez is already included")
else:
    print ("Veg lazeez not present adding to the list")
    tastydishes.extend (["veg lazeez"])
	
chinesedishes = ["Sweet corn soup", "Paneer Mongolian", "Schezwan Veg"]

print ("Adding the two lists using the + operator")
print (tastydishes + chinesedishes)

loneWolf = ["Karela Curry"]

print ("\n\nsingleton -", loneWolf)
print ("loneWolf multiplied by itself 5 times - ", loneWolf * 5)

print ("Count of Karela curry is - ", loneWolf.count("Karela Curry"))




