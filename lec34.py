# this lectures covers : Inheritance 

'''
Inheritance :  it is the process of creating a new class with features that belongs to the the parent class or
the class the it is inherited from it   

'''

class Person:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def dispaly(self):
        print("Name: ",self.name," ","ID: ",self.id)

class Teacher(Person):
    def __init__(self, name, id,salary):
        super().__init__(name, id)
        self.salary = salary
class Student(Person):
    def __init__(self,name,id,grade):
        super().__init__(name,id)
        self.grade = grade
# creating to objects from class Teacher and class Student        
Teacher1 = Teacher("Ahmad",1,2500)
Student1 = Student("Ali",5,'Good')
# display the name and id
print(Teacher1.dispaly())
print(Student1.dispaly())
