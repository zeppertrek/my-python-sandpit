# decoratorsinclasses.py
#
# decoratix.py            -  Intro to decorators           (1)
# decomoreco.py           -  Advanced decorators           (2)
# decoratewithclass.py    -  Class decorators              (3)
# decoratorsinclasses     -  Decorators inside a class     (4)
#


def jazzitup(myfunc):
    def wrapper(self, myage):
        print(":::X::: jazzitup  - {} ".format(myfunc.__name__))
        print(":::X::: jazzitup  - {} ".format (self))
        myfunc(self, myage)

    return wrapper


# Plugging in a decorator over here ( decorator placeholder 1)
class Cheesydecorators():

    def __init__(self):
        pass

    #
    @staticmethod
    def jazzupthename (myfunc):
        def wrapper (ref, myname):
            print (":::X::: Cheesydecorator1  - {} ".format(ref))
            myfunc(ref, myname)
        return wrapper


class Cheesyandclassy:

    # Plugging in a decorator over here ( decorator placeholder 2)
    def Cheesydecorator2(self):
        pass

    def __init__(self, name, age, gender, birthplace):
        # Note the indentation
        # These are all attributes / instance variables of the object
        self.name = name
        self.age = age
        self.gender = gender
        self.birthplace = birthplace

    # Applying a stand alone decorator to a method within a class
    @jazzitup
    def  setage(self, myage):
        self.age = myage

    # This decorator is contained within another class
    @Cheesydecorators.jazzupthename
    def setname(self, updatedname):
        self.name = updatedname

mycc = Cheesyandclassy ("Sanjiv", "50", "M", "Pune")

mycc.setage (20)
print ("Value of age attribute is now - {}".format (mycc.age))

mycc.setname("Sanjiv corrected")
print ("Value of name attribute is now - {}".format (mycc.name))




