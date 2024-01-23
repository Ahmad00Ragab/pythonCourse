# this lectures covers : Common Terms of OOP ==> Encapsulation

'''
Encapsulation :  it is the process of packaging the data(variables or attributes) and behaviors (methods) in a unit 
called a class and controlled using an access modifier  

'''

print("=================== Program1 ===================")
class Car:
    def __init__(self,name,fuel):
        self.__name    = name
        self.__fuel    = fuel
        self.maxFuel   = 90
    def setFuel(self,fuel):
        if(self.__fuel < self.maxFuel):
            fuel        = self.maxFuel - self.__fuel
            self.__fuel += fuel  
        else:
            print("Tank is FULL")
    def getFuel(self):
        return (self.__fuel)

# creating an object car1 from Car class
car1 = Car("BMW", 50)

car1.setFuel(10)  # Set additional 10 units of fuel
print(car1.getFuel())  # Should print 60

car1.setFuel(10)  # Set additional 10 units of fuel
print(car1.getFuel())  # Should print 70

print("=================== Program2 ===================")
class Bank:
    def __init__(self,cardHolder,CVV,balance):
        self.cardHolder = cardHolder    
        self.CVV = CVV    
        self.__balance = balance
        
    # a function to set the balance 
    def setBalance(self):
        Name    = input("Enter your Name: ")
        CVV     = input("Enter CVV      : ")
        balance = int(input("Enter the amount : "))
        if(self.CVV == CVV and self.cardHolder == Name):
            self.__balance += balance
        else:
            print("Unauthorized!")
    
    # a function to get the balance 
    def getBalance(self):
        Name = input("Enter your Name: ")
        CVV  = input("Enter CVV      : ")
        if(self.CVV == CVV and self.cardHolder == Name):
            print("Balance : ",self.__balance)
        else:
            print("Unauthorized!")
    
user1 = Bank("Ahmad",'123',500000)


# before adding new deposits
print("===== cheking balance =====")
print(user1.getBalance())

# add in the balance 
print("===== setting balance =====")
user1.setBalance()

# checking the balance 
print("===== cheking balance =====")
user1.getBalance()
