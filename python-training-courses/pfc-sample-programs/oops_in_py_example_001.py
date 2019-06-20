# oops_in_py_example_001.py 

# Defining a class to store attributes and methods related to a student 
class Student:

    # Class attribute
    student_group = 'STUDENT'

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
		
    def update_enrollment_status (self, enr_status):
        self.enr_status = enr_status

    # instance method
    def description(self):
        return "{} is {} years old and enr_status is {}".format(self.name, self.age, self.enr_status)
		
		

# Creating instances of the student class 
student1 = Student ("Ram", 22)
student2 = Student ("Laxman", 33)

# For each instance/object, invoking a method 
student1.update_enrollment_status ("WITHDRAWN")
student2.update_enrollment_status ("CANCELLED")

print (student1.description())
print (student2.description())

print (Student.student_group)