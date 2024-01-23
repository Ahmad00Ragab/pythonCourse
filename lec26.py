# this lec covers : Examples on Functions

'''
# program1
create function with 3 parameters (number1,number2,operation)
operation : add,substract,mulitply,divide

# program2
create a function accept any number of parameters then add them together 
(number1,number2,number3,...)

'''


# a function to make the required operation on the input numbers 
def makeOperation(num1,num2,op):
    result = 0
    if(op == '+'):
        result = num1+num2
    elif(op == '-'):
        result = num1-num2
    elif(op == '*'):
        result = num1*num2
    elif(op == '/'):
        result = num1/num2
    else:
        print("Invalid input operation!")
        return
    return result

# a function the required operation 
def chooseOperation():
    print("add ==> +")
    print("sub ==> -")
    print("mul ==> *")
    print("div ==> /")
    userChoice = input("Enter your choice : ")
    return userChoice

print("============ program1 ============")
# get the required operation from the user 
userChoice = chooseOperation()
# get the two numbers from the user 
num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))
# calculate the required operation
result = makeOperation(num1,num2,userChoice)
# display the result
print(result)

# a function that accepts any number of numbers and return the result of the sum 
def addNumbers(*numbers):
    result = 0
    for i in numbers:
        result +=i
    return result



print("============ program2 ============")
# first call
print(addNumbers(15,63,80,90))

# second call
print(addNumbers(35,63))

# Third call
print(addNumbers(100))


