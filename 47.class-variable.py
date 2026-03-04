# class variable = Shared among all instances of a class
#                  Define outside the constructor
#                  Allow you to share data among all objects created from that class

class Student:
    job:str = "Actor"
    class_year = 2024
    num_student = 0
    def __init__(self, name:str, age:str):
        self.name= name
        self.age = age
        Student.num_student += 1
        

student1 = Student("Spongebob", 30)
print(student1.name, student1.age, student1.job, student1.class_year, Student.num_student)

student2 = Student("Patrick", 35)
print(student2.name, student2.age, student2.class_year, Student.num_student)

print(Student.class_year, Student.num_student)
