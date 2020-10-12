# inheritoops

# Import for Abstract base classes
# Alternatively one can use, "from abc import ABC, abstractmethod"
import abc

# Use of abc.ABC means that the class is abstract and cannot be instantiated
#
class Spaceship (abc.ABC):

    #
    interplanetary_travel = "Y"
    #
    def __init__(self, ssg):
        self.spaceship_group = ssg

    @abc.abstractmethod
    def flush_warp_engines(self):
        pass

    @abc.abstractmethod
    def run_engine_check (self):
        pass

    # Defining a class method
    @classmethod
    def print_class_values(cls):
        print ("this is a class method")

    # Defining a static method
    @staticmethod
    def static_universe():
        print ("2020 is so static")


class Enterprise (Spaceship):

    def __init__(self, entmodel):
        super().__init__('ENTERPRISE-SS')
        self.enterprise_model = sclass

    def flush_warp_engines(self):
        print ( "Enterprise is flushing its warp engines - overriding of abstract method")

    def run_engine_check (self):
        print ( "Enterprise is flushing its warp engines -  overriding of abstract method")

# This will not work
# An abstract class has to be sub classed for instantiation
#absship = Spaceship()

myship = Enterprise("enterprise-spaceship")

myship.flush_warp_engines()
print ( "SC - {}  and MG - {} ".format (myship.spaceship_class, myship.model_group ))

myship.print_class_values()

myship.static_universe()