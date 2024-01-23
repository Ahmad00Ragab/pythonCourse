# this lec covers : strings

'''
strings : strings in python are immutable objects that you can't change their values
strngs  : can be put in 'single quotation ' "Double quotation"  "Triple quotation"

'''

'''
x    = "Ahmad"
#x[0] = 'a'   #error (not compilation because here there is no compiler ,there is an interpreter) 
print(x)
# writing a string with trible quotation
x =  "Ali"
print(x)

'''
# expressing the elements of the array or the string can be like 0 1 2 3 4 ... 
# or -(size-1) -(size-2 ) ..... -1
'''
x = "python"
print(x[0],x[-6]) 

print(x[1],x[-5]) 

print(x[2],x[-4]) 

print(x[3],x[-3]) 

print(x[4],x[-2]) 

print(x[5],x[-1]) 

'''

'''

# string methods : methods or functions that work on the string literals

# str.replace()  : replace part of the string or the whole string with new literal
# str.swapcase() : convert each character from lowercase to uppercase or vice versa 
# str.lower()    : convert the characters of the string from upper to lower 
# str.upper()    : convert the characters of the string from lower to upper 

#examples
y = "Ahmad"
# swap charcters case
print(y.swapcase())
# find the size of the string
print(len(y))
# convert the characters of the string from lower to upper 
print(y.upper())
# convert the characters of the string from upper to lower 
print(y.lower())

''' 

# string operations : make operations on the strings
 
#    +    :  string concatenation
#    *    :  string repetition
#   [ ]   :  string slicing
#   [:]   :  string Range slicing
#   in    :  string check  (check if character is in the string and return true if it is in)  

# string concatenation
str = "Ahmad Loves "
print(str + "programming")   # Ahmad Loves prgramming 

# string repetition
print(str*3 + "programming") # Ahmad Loves Ahmad Loves  Ahmad Loves programming

# string slicing
print(str[0],str[-1])        # A 

# string slicing in range
print(str[0:5])              # Ahmad

# checking on a string
print('v' in str)            # True



