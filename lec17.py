# this lec covers :  Examples on Conditionals

'''
compound condition:  
- if condition and condition :
- if condition or condition  :
- if not condition  


Exercise
write a program that displays the following menu, then acts accordingly: 
Enter you choice : 
1. Add two numbers
2. Get the Substract of two numbers
3. Get the multiply of two numbers

the program should give an error message for invalid inputs

# '''
# # program 1
# student1 = "Boy"
# student2 = "Girl"
# if(student1 == "Boy"):
#     print("Sudent1 is a Boy")
# else:
#     print("Student1 is a Girl")


# #progam 2
# if student2 == "Girl":
#     print("Studen2 is a Girl")
# elif student2== "Boy":
#     print("Student2 is a Boy")
# else:
#     print("Unknown")

#Exercise 

print("1. Add two numbers")
print("2. Get the Substract of two numbers")
print("3. Get the multiply of two numbers")

x = int(input("Enter Your Choice: "))
if   x==1:
    number1 = (int)(input("Enter number1: "))
    number2 = (int)(input("Enter number2: "))
    print("Result : ",number1+number2)
elif x==2:
    number1 = (int)(input("Enter number1: "))
    number2 = (int)(input("Enter number2: "))
    print("Result : ",number1-number2)
elif x==3:
    number1 = (int)(input("Enter number1: "))
    number2 = (int)(input("Enter number2: "))
    print("Result : ",number1*number2)
else:
    print("Invalid input, Error!")