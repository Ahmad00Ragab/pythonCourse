# this lec covers :  training on loops   

''' 
# prgram 1
write a program that prints out numbers from 0 to 10 in ascending order 

# program 2
write a program that prints out numbers from 0 to 10 in descending order

# program 3
write a program to calculate the sum of first 10 natural number

# program 4
write a program that prints the sum of the even and odd integers

# program 5
create this list = [15,81,5,17,20,21,13]
print all number that divisible by 5 using loop 

'''

print("============ Program1 ============")
# program 1
# print the values from 1 to 10 in ascending order 
for i in range(1,11):
    print(i)
print("============ Program2 ============")
# program 2
# print the values from 10 to 1 in decending order 
i = 10
while(i>0):
    print(i)
    i -= 1
print("============ Program2 ============")
# program 2
# print the values from 10 to 1 in decending order 

for i in reversed(range(1,11)):
    print(i)
print("============ Program3 ============")

sum = 0
for i in range(1,11):
    sum +=i
print("Sum : ",sum)

print("============ Program4 ============")

sumEven = 0
sumOdd  = 0
for i in range(1,11):
    if(i%2 == 0):
        sumEven += i
    else :
        sumOdd +=i
print("Sum Even: ",sumEven)
print("Sum Odd : ",sumOdd)

print("============ Program5 ============")
list = [15,81,5,17,20,21,13]
print("list : ",list)
for i in list:
    if(i%5 == 0):
        print(f"{i}  ",end="")
print("") # don't print any thing 

name = "John"
age = 30

# Using f-string to format a string
sentence = f"My name is {name} and I am {age} years old."

print(sentence)
