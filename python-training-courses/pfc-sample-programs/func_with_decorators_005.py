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

def another_funcky_func(*args):
    def delta_funcky_001(*args):
        summa = 0
        for i in args:
            summa = summa + i
        print ("Inside another_funcky_func.delta_funcky_001 - summa value ", summa )
    return delta_funcky_001(*args)


my_funcky_func = another_funcky_func(1,2,3,4,5,6,7)


def another_fluncky_func(*args):
    def delta_fluncky_001(*args):
        summa = 0
        for i in args:
            summa = summa + i
        print ("Inside another_funcky_func.delta_funcky_001 - summa value ", summa )
    return delta_fluncky_001


my_fluncky_func = another_fluncky_func()

my_fluncky_func(2,2,2,2,2)