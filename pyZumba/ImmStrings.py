# ImmStrings.py
# Immutability of Strings
# Such an object cannot be altered. A new object has to be created if a different value has to be stored. T
# They play an important role in places where a constant hash value is needed, for example as a key in a dictionary

def main():
    str1 = "Sanjiv"
    print (str1) 
    str2 = str1
    print (str2)
	str1 = "Sanjiv222"
	print ("{} str1 and {} str2".format(str1, str2))

main()