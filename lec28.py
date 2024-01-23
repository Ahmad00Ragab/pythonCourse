# this lectures covers : Classes & Objects 

'''
what is class:  it is the blueprint of the object or a data structure that contain the attributes 
and behaviours of the object 

what is a constructor :  it is a method that is defined inside the class and this function (constructor)
is called automatically once a new object of this class is created


'''

class Car:
    def __init__(self,name,color,price,speed):  # constructor : initialization function 
        self.name  = name                       # ref current object  
        self.color = color
        self.price = price                      # instance attribute 
        self.speed = speed

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
car2 = Car("Mercedes","RED",1200000,200)       # car2 is an instance or an object 
print(f"{car2.name}" ,"  ", end="")
print(f"{car2.color}","  ", end="")
print(f"{car2.price}","  ", end="")
print(f"{car2.speed}","  ", end="")

print("")