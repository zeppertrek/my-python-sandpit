#
#
#
# setter, getter and property
#
# metaclass = ABCMeta or abc.ABC when creating the class
#
# @property decorator
# @property along with @abstractmethod
#
# @<attribute_name>.setter
# @<attribute_name>.setter along with @abstractmethod
#
# @classmethod along with @abstractmethod
#
# @staticmethod along with @abstractmethod


from abc import ABCMeta, abstractmethod


# metaclass = ABCMeta can be substituted by abc.ABC
class AbstactClassCSV(metaclass=ABCMeta):


    def __init__(self, path, file_name):
        self._path = path
        self._file_name = file_name

    # This acts as the getter
    @property
    @abstractmethod
    def path(self):
        pass


    @path.setter
    @abstractmethod
    def path(self, value):
        pass


    # this acts as the getter
    @property
    @abstractmethod
    def file_name(self):
        pass


    @file_name.setter
    @abstractmethod
    def file_name(self, value):
        pass


    @abstractmethod
    def display_summary(self):
        pass


    @classmethod
    @abstractmethod
    def display_class_summary():
        pass


    @staticmethod
    @abstractmethod
    def display_static_data():
        pass


##
##
## AbstactClassCSV.register - What does this do ?
##
class CSVFile(AbstactClassCSV):

    def __init__(self, path, file_name):
        super().__init__(path, file_name)


    @property
    def path(self):
        print("This is the implementation of abstract method for property <path> - {} ".format(self._path))
        return self._path

    @path.setter
    def path(self, value):
        print("This is the implementation of abstract method for property <@path.setter> ")
        self._path = value

    @property
    def file_name(self):
        print("This is the implementation of abstract method for property <file_name>  - {}".format(self._file_name))
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        print("This is the implementation of abstract method for property <@file_name.setter> ")
        self._file_name = value


    # @abstractmethod
    def display_summary(self):
        print(" Path - {} and file_name - {}".format(self._path, self._file_name))


    # @classmethod
    # @abstractmethod
    def display_class_summary():
        print(" Print class related data ")


    # @staticmethod
    # @abstractmethod
    def display_static_data():
        print(" Print static related data ")


myFile = CSVFile("D:\SANJIV", "sanjiv.py")

print(myFile.path)

print(myFile.file_name)

myFile.file_name = "changedfilename.pypy"
print(myFile.file_name)


##################################################################################
##################################################################################

