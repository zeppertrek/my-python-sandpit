# String_var_example_002.py
# This program contains a few examples of string functions 

saying = "the quick brown fox jumped over the really lazy dog"

singleWord = "farrago"

print (singleWord + " singleWord capitalized is ", singleWord.capitalize())

print (saying + " capitalized is ", saying.capitalize())

print (saying + " contains only alphabets is ", saying.isalpha())

myNumberStr = '01233333333333333445555555555'

print (myNumberStr + " contains only numbers is ", myNumberStr.isnumeric())

print ("Length of singleWord is ", len (singleWord))

print (singleWord + " reversed is ", ''.join(reversed(singleWord)))


# Range Slicing
z1 = singleWord[2:] 

print(z1, "   this is a slicing of singleWord[2:]" )

if ( "fully-loaded-herby-pizza".find ("herby") >= 0 ):
    print ("herby is really part of fully-loaded-herby-pizza")
	
print ("This is really nice in a Pizza ",  "Veg Supreme Pizza with Olives"[23:] )
