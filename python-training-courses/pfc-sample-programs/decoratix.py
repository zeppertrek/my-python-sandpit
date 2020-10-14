# decoratix.py
# All about Python decorators

#################################################################################
import functools

print (":::1.1::: The basics of decorators - Understanding the concept")

def  decorama ( funcster ):
    #
    def innerfunc():
        #
        print (":::1.1::: decorama-->innerfunc-PRE")
        funcster()
        print (":::1.1::: decorama-->innerfunc-PRE- DONE DUNNA DUN")
    return innerfunc


def inneedofadeco():
    print (":::1.1::: I am in need of a deco - ")

inneedofadeco()
#
print (":::1.1::: Now for the decoration magic")
inneedofadeco = decorama ( inneedofadeco )
inneedofadeco()

# There is side effect.  The function after the decoration operation has lost its bearings i.e. name
print ( ":::1.1::: name of the function after the decoration ---- {} ".format(inneedofadeco.__name__))

################################################################################


def  decounwrapped ( funcster ):
    #
    print (":::1.2::: decounwrapped  - {} ".format (funcster.__name__))
    return funcster

@decounwrapped
def eazzypeazzy():
    print (":::1.2::: Example of an unwrapped decorator  - ")

eazzypeazzy()


####################################################################################
print ("PART 2 ::: Understanding the concept of decorators a bit more")

def  decoranama ( funcster, x,y ):
    #
    def innerfunc():
        #
        print ("decoranama-->innerfunc-PRE")
        funcster(x,y)
        print ("decoranama-->innerfunc-PRE- DONE DUNNA DUN")
    return innerfunc


def needfordecorum(x,y):
    print ("I am in need of a deco - {} --- {} ".format(x,y))

needfordecorum("##","!!")

print ("Now for the decoration magic")
needfordecorum = decoranama ( needfordecorum, "Alpha", "Gamma" )
needfordecorum()

print ( "name of the function after the decoration ---- {} ".format(inneedofadeco.__name__))

#############################################################################################################

print ("PART 3 ::: Decorators - The first use of a decorator using the @ syntax ")

def  decormate (funcster):
    #
    def innerfunc():
        #
        print (":::3:::decormate-->innerfunc-PRE")
        funcster()
        print (":::3::: decormate-->innerfunc-PRE- DONE DUNNA DUN")
    return innerfunc

@decormate
def justtoosimple():
    print (":::3:::I am just too simple hence in need of a decormate ")

justtoosimple()


#############################################################################################################

print ("PART 4 ::: Decorators -  Function to be decorated accepts parameters ")

def  decormator (funcster):


    # This will preserve information about the original function.
    @functools.wraps (funcster)
    def innerfunc(*args, **kwargs):
        #
        print (":::4:::decormator-->innerfunc-PRE")
        funcster(*args, **kwargs)
        print (":::4::: decormator-->innerfunc-PRE- DONE DUNNA DUN")
    return innerfunc

@decormator
def justtoozzimple(*args, **kwargs ):
    print (":::4:::I am justtoozzimple hence in need of a decormator ")

justtoozzimple(1,2)


#############################################################################################################

print ("PART 5 ::: Decorators -  Function to be decorated accepts parameters ")
print ("PART 5 ::: Decorators -  Different ways of passing values to the func. 2b decorated ")
print ("PART 5 ::: Decorators - Remember the same decorator might be used for multiple functions")


def  decormator (funcster):
    #

    # make sure the wrapper function returns the return value of the decorated function
    # This will preserve information about the original function.
    @functools.wraps (funcster)
    def innerfunc(*args, **kwargs):
        #
        print (":::5:::decormator-->innerfunc-PRE")
        funcster(*args, **kwargs)
        print (":::5::: decormator-->innerfunc-PRE- DONE DUNNA DUN")
    return innerfunc

@decormator
def justtoozzimple(*args, **kwargs ):
    print (":::5:::I am justtoozzimple hence in need of a decormator ")

justtoozzimple(1,2)

@decormator
def rimplesimpleton( x,y ):
    print (":::5:::I am rimplesimpleton hence in need of a decormator ")

rimplesimpleton(1,2)

@decormator
def ipsydipsy():
    print (":::5:::I am ipsydipsy hence in need of a decormator ")

ipsydipsy()


#############################################################################################################

print ("PART 6 ::: Decorators -  Function to be decorated accepts parameters ")
print ("PART 6 ::: Decorators -  Different ways of passing values to the func. 2b decorated ")
print ("PART 6  ::: Decorators - Remember the same decorator might be used for multiple functions")
#
#
# Why does one need the inner/nested func ?
# To leverage the concept of a closure. How ?
#  simpledekor = dekor6 ( simpledekor)   -- This happens due to the @ decoration
#           @dekor6
#           def simpledekor().......
#
#  simpledekor now has a reference to the nested wrapper function defined in dekor6 (say wrapper)
#  Because of closures, the wrapper function remembers that the function passed
#  from the enclosing scope is actually simpledekor
#  so now the simpledekor execution statement with the arguments is actually
#  the wrapper function call with the same set of arguments
#  So    simpledekor (..., ..., ....) is actually wrapper (..., ..., ...)
#
#


def  dekor6 (funcster):
    #

    # The function to be decorated receives its arguments through the wrapper
    # This will preserve information about the original function.
    @functools.wraps (funcster)
    def wrapper( *args, **kwargs):
        #
        print (":::6::: {} ---- {}".format (args, kwargs))
        funcster(*args, **kwargs)

    for i in wrapper.__closure__:
        print(i.cell_contents)
    return wrapper

@dekor6
def simpledekor(*args, **kwargs ):
    print (":::6:::I am simpledekor hence in need of a decormator ")


simpledekor(1,2,3,4,5,6,7,8,9,10)

@dekor6
def rimplecrimple(*args, **kwargs):
    print (":::6:::I am rimplecrimple hence in need of a decormator ")

rimplecrimple([1,2,3,4,5], {"1" : 1, "2" : 2})

@dekor6
def ipsydipsy6(*args, **kwargs):
    print (":::6:::I am ipsydipsy6 hence in need of a decormator ")

ipsydipsy6()



#############################################################################################################

print ("PART 7 ::: Decorators -  Function to be decorated accepts parameters ")
#
#

def  bellsandwhistles (myfunc):
    #
    # The function to be decorated receives its arguments through the wrapper
    # This will preserve information about the original function.
    @functools.wraps (myfunc)
    def wrapper( *args, **kwargs):
        #
        print (":::7::: pre statemnt 1")
        retval = myfunc(*args, **kwargs)
        print (":::7::: post statemnt 1")
        return retval
    return wrapper

@bellsandwhistles
def wrapmewell(*args, **kwargs ):
    argscount = len(args)
    kwargscount = len(kwargs)
    return argscount + kwargscount


print ( ":::7::: Computed value - {}".format (wrapmewell( *[1,2,3,4,5,6,7,8,9,10],  **{"1" : 1, "2" : 2} ) ) )
