# this lectures covers : Instance & Class Methods  

'''
Instance method : it is a method that defined with format like :
def fun(self,parameters):
    # attribute 1 
    # attribute 2
    
class method    : it is  a method that belongs to the class itsself and  defined with format like:
@classmethod
def fun(class):
    return class()
'''

class Factory:                    # class attribute  and it is shared between objects      
                      
    def __init__(self,size):  # constructor : initialization function 
        self.size  = size                       # ref current object  
   
    @classmethod
    def small(cls):
        return cls('S')
    @classmethod
    def Medium(cls):
        return cls('M')
    @classmethod
    def Large(cls):
        return cls('L')
    @classmethod
    def X_Large(cls):
        return cls('XL')

# creating a some objects # 
T_Shirt1 = Factory.small()
T_Shirt2 = Factory.Medium()
T_Shirt3 = Factory.Large()
T_Shirt4 = Factory.X_Large()

print(T_Shirt1.size)
print(T_Shirt2.size)
print(T_Shirt3.size)
print(T_Shirt4.size)
