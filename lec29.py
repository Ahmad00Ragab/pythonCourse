# this lectures covers : instance attributes  &  class attributes  

'''
instance attribute : it is an attribute that belongs to the intance that is created and it is define inside constructor 
class    attribute : it is an attribute that belongs to the class itself and it must be initialized 

'''


class Car:
    
    numberOfCars = 0                            # class attribute  and it is shared between objects 
     
    def __init__(self,name,color,price,speed):  # constructor : initialization function 
        self.name  = name                       # ref current object  
        self.color = color
        self.price = price                      # instance attribute 
        self.speed = speed
        Car.numberOfCars +=1

print("======= First Object =======")
# defining an object and intializing its constructor
# object1 
car1 = Car("Fiat","Black",1400000,250)          # car1 is an instance or an object 
print(f"{car1.name}" ,"  " ,  end="")
print(f"{car1.color}","  ", end="")
print(f"{car1.price}","  ", end="")
print(f"{car1.speed}","  ", end="")
print("")
# defining an object and intializing its constructor 
# object2 
print("======= Second Object =======")
car2 = Car("Mercedes","RED",1200000,200)       # car2 is an instance or an object 
print(f"{car2.name}" ,"  ", end="")
print(f"{car2.color}","  ", end="")
print(f"{car2.price}","  ", end="")
print(f"{car2.speed}","  ", end="")
print("")
print("======= Class Attribute =======")
print("Number Of Cars: ",Car.numberOfCars)