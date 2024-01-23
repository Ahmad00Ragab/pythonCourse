# this lec covers :  Loops 

'''
For Loop 

for iterator in range(lower : upper)
    # do something #

'''

# display the numbers from 1 to 100
for i in range(1,101):
    print(i)

print("======================")

# display the characters from a to z and A to Z 
for i in range (ord('a'),ord('z')+1):
    print(chr(i),"     ",chr(i-32)) # printing the characters from a   A  to   z    Z 


print("======================")
# create a list and iterate over it and display its content by using for loop 
List = ["Ahmad","Hisham","Mourad","Raafat","Mahmoud"]
for i in List:
    print(i)
