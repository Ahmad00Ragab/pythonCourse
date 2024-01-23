# this lec covers : trainings on last lectures 

'''
# program 1
 write a program that creates three variables: student name, graduation year
,and letter grade. Then print the three values in one line 

# program 2
 write a program that creates three variables: student name, graduation year
,and letter grade. Then print the three values in different lines 

# program 3
 write a program that slice this word Ahmed to 3 lines by index 
first line : Ahm
second line: ed
third line : mha

# program 4
remove sybmols @$#Ahmed$#!
output: Ahmed
'''

x =  "Ahmad"
y =  2019
z =  "C"

# program 1
print(x+" "+(str)(y)+" "+z)

# program 2
print(x+"\n"+(str)(y)+"\n"+z)



# program 3
str = "Ahmed"

print(str[0:3]) # Ahm
print(str[3:5]) # ed

print(str[2]+str[1]+str[0].lower()) # mha

# program 4
str = "@$#Ahmed$#!"
str_out = ""
for char in str:
    if(char.isalpha()):
        str_out +=char
print(str_out)

        

