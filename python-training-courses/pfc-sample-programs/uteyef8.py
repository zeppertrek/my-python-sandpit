# uteeyefate.py


# By default, Python 3 uses UTF-8 for string encoding
# Thank your lucky stars that the snake can digest strings in this way
#
# Declaring a string variable with \u notation to store characters from other languages
str1 = '\u0905\u0906\u0907\u0908\u0909\u0910'
print (str1)

#Similar to the above with a different set of characters
strrussian = '\u0420\u043e\u0441\u0441\u0438\u044f'
print (strrussian)

# Storing devanagiri script characters
str2 = "अआइईउऐ"

print (str2)
print ("Length of str2 printed above", len(str2))

# Storing chinese script characters
str3 = '你好'
# printing the length
print(len(str3))

# Looping
for i in str3:
    print (i)

for j in str1:
    print (j)

# Concatenating strings from different languages
print ( str1 + str2 + str3 + strrussian + "sweffrrrr44441234@#$$" + '2131232133!!!!')