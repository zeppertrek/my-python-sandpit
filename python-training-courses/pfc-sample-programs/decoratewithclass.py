
print ("Execution start stats - {}",format (__name__))


class decoratorclass1:

    def __init__(self, f):
        self.f = f

    # This is important
    def __call__(self):
        print(":::1::: Decorating", self.f.__name__)
        self.f()

@decoratorclass1
def func1():
    print(":::1::: inside func1()")

func1()

############################################


class decoratorclass2:

    def __init__(self, f):
        self.f = f

    # This is important
    def __call__(self, *args, **kwargs):
        print(":::2::: Decorating", self.f.__name__)
        self.f()

@decoratorclass2
def func2(*args, **kwargs):
    print(":::2::: inside func2()")

func2(*[1,2], **{"1":1})


############################################
#
#
#  The class decorator chain reaction (CDCR)
#
#  decobject = decoratorclass3 (*cdargs, **cdwargs)
#  This is possible only because of __call__
#  func3 = decobject (func3)
#  func3 <-------- wrapper !
#  func3 (...., ....) <====> wrapper ( ..., ....)
#
#decobject =  decoratorclass3 (*[1,2,3,4], **{"qwerty" : 1})
#func4444 = decobject (func4444)
#func4444 (*[1,2], **{"1":1})

# Somewhere an object is getting created. How do we access it ?.
# What are the advantages of class decorators over function decorators

class decoratorclass3:

    def __init__(self, *cdargs, **cdwargs):
        self.cdargs = cdargs
        self.cdwargs = cdwargs
        print(":::3::: Inside __init__ part of the decorator chain reaction (DCR) !")

    # This is important
    def __call__(self, func):
        def wrapper (*args, **kwargs):
            print(":::3::: wrapper DCR -- {}".format(func.__name__))
            print(":::3::: wrapper DCR cdargs - {} ".format(self.cdargs))
            print(":::3::: wrapper DCR cdwargs - {} ".format(self.cdwargs))
            func (*args, **kwargs)

        print(":::3::: returning the wrapper as part of DCR ")
        return wrapper

@decoratorclass3(*[1,2,3,4], **{"qwerty" : 1} )
def func3(*args, **kwargs):
    print(":::3::: inside func3() - {}  ## {}".format(args, kwargs))

func3(*[1,2], **{"1":1})

for i in func3.__closure__:
    print(i.cell_contents)


