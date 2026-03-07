# Class methods = Allow operations related to the class itself
#                 Take (cls) as the first parameter, which represents the class itself.
#
#   Instancc methods = Best for operations on instances of the class (object)
#   Static methods = Best for general utility functions that do not need access to class data
#   Class methods = Best for class-level data or require access to the class itself



class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        # Everytime we create a Student Object it will count attribute/variable count
        Student.count += 1
        Student.total_gpa += gpa
        # This is instance method
    def get_info(self):
        return f"{self.name} {self.gpa}"
        
    @classmethod
    def get_count(cls):
        return f"Total number of students: {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average gpa: {cls.total_gpa / cls.count:.02f}"

    
    
student1 = Student("Bob", 3.2)
student2 = Student("Rick", 2.2)
student3 = Student("Steve", 4.0)
        
print(Student.get_count())
print()
print(Student.get_average_gpa())
