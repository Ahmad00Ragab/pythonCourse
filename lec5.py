# this lec covers : Data Types
'''
tex           type : str
numberic      type : int , float
boolean       type : bool
sequence      type : list,tuple,set
mapping       type : dict

'''

# numberic      type : int, float
print("4                     : ",type(4))
print("4.5                   : ",type(4.5))
        
# boolean       type : bool
print("True                  : ",type(True))
        
# sequence/set  type :list,tuple
var1 = {10,20,66}           
var2 = ["Ahmad","Mohamed"]
var3 = (1,2,3)           
print("{10,20,66}            : ",type(var1))
print("[10,20,66]            : ",type(var2))
print("(1,2,3)               : ",type(var3))
      
# mapping       type : dict
var4 = {"Name":"Ahmad", "Age" : 28}
print("Name: Ahmad, Age: 28  : ",type(var4))
