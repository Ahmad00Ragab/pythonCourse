# this lec covers :  Nested if 

'''
Nested if ==> if inside if 
'''

age = int(input("Enter your Age: "))
if (age > 0):
    
    if(age >= 18 and age <= 60):
        print("Welcome, Adult!")
    elif(age>60):
        print("You are over age")
    else:
        print("Your are under Age")

else:
    print("Invalid age")