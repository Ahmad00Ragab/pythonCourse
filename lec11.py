# this lec covers : Mathematical Operations

'''
Operators:
 + : add two numbers
 - : sub two numbers
 * : mul two numbers
 / : div two numbers
 #################
 % : getting the reminder after div two numbers
 important note: unlike C language, when we use the % operator with negative numbers,
 the result follows the sign of the divisor  
 #################
'''

# degrees of a student 
subject1 = 50
subject2 = 40

print("subject1: ",subject1)
print("subject2: ",subject2)

# print the result (+ operator with strings : concatenate the strings )
print("Total scor is : "+ (str)(subject1 + subject2) + " Average is : "+str((subject1+subject2)/2))
# -  operator
print("Sub : ",(subject1-subject2))
# *  operator
print("mul : ",(subject1*subject2))
# /  operator
print("div : ",(subject1/subject2))
# %  operator
print("mod : ",(subject1%subject2))

#special cases of %
print("-5 %  2 = ",(-5%2))  # sign of result following the divisor +2  ==>  1
print(" 5 % -2 = ",( 5%-2)) # sign of result following the divisor -2  ==> -1
print("-5 % -2 = ",(-5%-2)) # sign of result following the divisor -2  ==> -1






