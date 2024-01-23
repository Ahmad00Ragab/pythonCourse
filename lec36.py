# this lectures covers :  Abstraction 

'''
Abstraction : it is the process in which you hide the unncessary details from the user
we use it when we create a class that contains the headers for methods and these methods 
are implemented inside the inherited classes 

'''

from abc import ABC, abstractmethod


class Vehicle: 
    @abstractmethod
    def moveForward(self):  # the prototype of the method that is defined in any other class 
        pass
    
    @abstractmethod
    def moveBackward(self):
        pass
    
    @abstractmethod
    def turnLeft(self):
        pass
    
    @abstractmethod
    def turnRight(self):
        pass



class Car(Vehicle):

    def moveForward(self):  # the definition of the method that is defined in any other class 
        print("Car Move Forward")
    
    def moveBackward(self):
        print("Car Move Backwrod")

    def turnLeft(self):
        print("Car Turn Left")

    def turnRight(self): 
        print("Car Turn Right")

class Moto(Vehicle):

    def moveForward(self):  # the definition of the method that is defined in any other class 
        print("Moto Move Forward")
    
    def moveBackward(self):
        print("Moto Move Backwrod")

    def turnLeft(self):
        print("Moto Turn Left")

    def turnRight(self): 
        print("Moto Turn Right")

# ==== #
car1  = Car()
moto1 = Moto()
print(car1.moveForward())
print(moto1.moveForward())
print(car1.moveBackward())
print(moto1.moveBackward())
# ==== #