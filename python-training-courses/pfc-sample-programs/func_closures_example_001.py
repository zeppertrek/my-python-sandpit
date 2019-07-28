#
# func_closures_example_001.py
# 
# func_with_real_decorators_005.py provides an introduction to closures. Let us take it further in this program
# 
# This is an interesting concept. 
#
####################################################################################################
#
# 
#
def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

# Multiplier of 3
times3 = make_multiplier_of(3)

# Multiplier of 5
times5 = make_multiplier_of(5)

# Output: 27
print(times3(9))

# Output: 15
print(times5(3))

# Output: 30
print(times5(times3(2)))

print ( "make_multiplier_of.__closure__" , make_multiplier_of.__closure__)
print ("times3.__closure__", times3.__closure__)
print ("times5.__closure__", times5.__closure__)
print ("times3.__closure__[0].cell_contents", times3.__closure__[0].cell_contents)
print ("times5.__closure__[0].cell_contents", times5.__closure__[0].cell_contents)

#######################################################################################################
# With multiple args 


def i_take_many_args(n1, n2, n3, n4, n5):
    def add_and_multiply(x1, x2, x3):
        return ( (x1 + x2 +x3 ) *  (n1+n2+n3+n4+n5))
    return add_and_multiply


z1 = i_take_many_args(1,1,1,1,1)

# Multiplier of 5
z2 = i_take_many_args(1,2,3,4,5)

# Output: 
# When z1 is invoked the arguments to the enclosing function are remembered 
print(z1 (1,1,1))

# Output: 
print(z2(2,2,2))

print ( "i_take_many_args.__closure__" , i_take_many_args.__closure__)
print ("z1.__closure__", z1.__closure__)
print ("z1.__closure__", z2.__closure__)

#
# A tuple of objects . Specifically a tuple of cells 
print (" Type of z1.__closure__ is ", type(z1.__closure__))
# 

for x in z1.__closure__:
    # x belongs to the cell class 
    print (type(x))
    print (x.cell_contents) 

for y in z2.__closure__:
    print (y.cell_contents)
	


#######################################################################################################
# With *args and **kwargs 


def too_many_args(*args1, **kwargs1):
    def any_random_stuff(*args2, **kwargs2):
        #return ( (len (args2) + len(args1) ) *  (len (kwargs1) + len(kwargs2)))
        for xxyy in args1:
            print (xxyy)
        for xxyy in args2:
            print (xxyy)
        return 1
    return any_random_stuff

yyz10 = [1,2,3,5]
yyz20 = {"1":"sanjiv", "2":"ananya"}
zz1 = too_many_args(*yyz10, **yyz20)

# 
yyz101 = [3,9,15]
yyz201 = {"8":"rohit", "7":"priyaa"}
zz2 = too_many_args(*yyz101, **yyz201)

# Output: 
# When zz1 is invoked the arguments to the enclosing function are remembered 
pc = [1,2,3,4]
dc = {"1":"z", "2":"p"}
print(zz1 (*pc, **dc))

# Output: 
pc = [1,2,3,4,5,6]
dc = {"1":"z", "2":"p"}
print(zz2(*pc, **dc))

print ( "too_many_args.__closure__" , too_many_args.__closure__)
print ("zz1.__closure__", zz1.__closure__)
print ("zz1.__closure__", zz2.__closure__)

#
# A tuple of objects . Specifically a tuple of cells 
print (" Type of zz1.__closure__ is ", type(zz1.__closure__))
# 

for x in zz1.__closure__:
    # x belongs to the cell class 
    print (type(x))
    print (x.cell_contents) 

for y in zz2.__closure__:
    print (y.cell_contents)
	






