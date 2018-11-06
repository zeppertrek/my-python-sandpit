# declaring_variables_example_007.py
#
# floats and ints

myfloatNum1 = 7.0234
print(myfloatNum1)
myfloatNum2 = float(199907.791)
print(myfloatNum2)

print ("--------------------------")
print ("type of myfloatNum1 and myfloatNum2 are ", type(myfloatNum1), type(myfloatNum2))

x1 = 1234567
x2 = 3456

# This should give you a float value
y1 = x1 / x2


print ("y1 is and type(y1) is ", y1, type(y1))

# Rounding off to two decimals
g = float("{0:.2f}".format(y1))

print ("Rounded off to two decimals : ", g)