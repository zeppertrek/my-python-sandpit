#func_with_decorators_005.py

# This contains logic that lays the groundwork for function and class decorators 
# func_with_decorators_001.py , func_with_decorators_002.py, func_with_decorators_003.py, func_with_decorators_004.py, func_with_decorators_005.py 
# These 5 programs play around with functions.  Some examples can be really weird 


def func1(num1):
    numxx = 100 + num1 
    print ( numxx)
 
x1 = func1(1)
x2 = func1(2)
#
print (id (x1))
print (id (x2)) 

#
#



################################################################################################################
def i_return_a_func(*args):

    def delta_func_001():
        print("Hello-000000111111111111")

    def delta_func_002():
        print("Hello-000000222222222222")

    def delta_func_003():
        print("Hello-000000333333333333")

    def delta_func_004():
        print("Hello-000000444444444444")

    summa = 0 
	 
    for i in args:
        summa = summa + i
    if summa == 1 :
        ret_func_name = delta_func_001
    elif summa == 2:
        ret_func_name = delta_func_002
    elif summa == 3:
        ret_func_name = delta_func_003
    else:
        ret_func_name = delta_func_004	    
    return ret_func_name
	

#
my_ret_func1 = i_return_a_func(0,1)
my_ret_func1()
#
#
my_ret_func1 = i_return_a_func(0,1,1)
my_ret_func1()
#
#
my_ret_func1 = i_return_a_func(0,1,1,1)
my_ret_func1()
#
#
my_ret_func1 = i_return_a_func(0,1,1,1,1)
my_ret_func1()
#
################################################################################################


#################################################################################################
def another_funcky_func(*args):
    def delta_funcky_001(*args):
        summa = 0
        for i in args:
            summa = summa + i
        print ("Inside another_funcky_func.delta_funcky_001 - summa value ", summa )
    return delta_funcky_001(*args)


my_funcky_func = another_funcky_func(1,2,3,4,5,6,7)
###################################################################################################






################################################################################################################

def another_fluncky_func(*args):
    def delta_fluncky_001(*args):
        summa = 0
        for i in args:
            summa = summa + i
        print ("Inside another_funcky_func.delta_funcky_001 - summa value ", summa )
    # 
    # Observe the difference when the return value omits the parentheses ()
    #
    return delta_fluncky_001


my_fluncky_func = another_fluncky_func()

my_fluncky_func(2,2,2,2,2)

#################################################################################################################3



#
# This is interesting 
# 
def finkertyfonk(x):
    def giddygoat(y):
        return y + x + 3 
    return giddygoat


# What do niff1 and niff2 really hold ? 
# Something strange is happening here 
# 
niff1 = finkertyfonk(1)
niff2 = finkertyfonk(9)


print("niff1", niff1)
print("niff1", niff2)

# 
#  Is this what Python means by closures as 1 and 9 ( "x" parameter ) is being remembered/stored 
# 
print("niff1(1)", niff1(2))
print("niff1(2)", niff2(10))



####################################################################################################
#
# Closures 
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


