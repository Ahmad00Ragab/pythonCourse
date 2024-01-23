# this lectures covers : Static Methods  

'''
Static method : it is a method that belongs to the class itself not the the instance that is created from this class
and it is defined on the following format: 
@staticmethod
def fun(parameters):
    return (return value)

'''

print("=============== Example1 ===============")
class Math:       

    def __init__(self,x,y):
        self.x = x           
        self.y = y   
    @staticmethod
    def add2(x,y):
        return (x+y)
    
    @staticmethod
    def add3(x,y,z):
        return (x+y+z)


result = Math.add2(3,5)
print("Result: ",result)


print("=============== Example2 ===============")
class Person:       

    def __init__(self,name,age):
        self.name = name           
        self.age  = age   
    
    # static method that belongs to the class itsself not to any instance 
    @staticmethod
    def compare(object1,object2):
        if isinstance(object1,Person) and isinstance(object2,Person):
            if object1.name == object2.name  and object1.age == object2.age:
                print(" Same Person ")
            else:
                print("Not the same Person")
        else:
            print(" Invalid input ")

person1 = Person("Ahmad",28)
person2 = Person("Ahmad",28)

# calling Compare "static method of Person class"  
Person.compare(person1,person2)

x = 10
y = 20

# give wrong inputs to the Compare Method   
Person.compare(x,y)


