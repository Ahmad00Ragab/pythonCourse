# this lec covers :  trainings on Lists
'''
Exercise1:

Create list with 5 values then :
print the first value
print the last value
print the foruth value 

Exercise2 : 
create lis with any 2 values then : 
add another      2 values 
delete the first 2 values

Exercise3 :
create a list with any 3 values 
create another list with 4 values
add 2 lists each other 

Exercise4:
create list with any random values then:
sort  them 
count them 

Exercise5:
create list:
students = ["Ahmed","Ashraf","Mohamed",["Ali","Hany","Fareed"]]
then :
Output = Ali Fareed

'''


print("\n============= Exercise1 =============")
# Exercise 1
# creating a list 
Numbers  = [100,200,300,400,500]
print(Numbers)
print("First  Value : ",Numbers[0])
print("Last   Value : ",Numbers[-1])
print("Fourth Value : ",Numbers[3])


print("\n============= Exercise2 =============")
# Exercise 2
# creating a list 
Numbers  = [100,200]
print(Numbers)
# add two values
Numbers.append(1000)
Numbers.append(2000)
# display the list after adding two values
print(Numbers)
# removing the two numbers
Numbers.remove(Numbers[0])
Numbers.remove(Numbers[0])
# display the list 
print(Numbers)

print("\n============= Exercise3 =============\n")
# Exercise 3
List1 = [1,2,3]
print("List1: ",List1)
List2 = [4,5,6,7]
print("List2: ",List2)
List3 = List1 + List2
print("List3: ",List3)

print("\n============= Exercise4 =============\n")
#Exercise4
List = [5,8,9,66,8,210,364,70,-63,66]
print("Before Sorting: ",List)
# sort the list 
List.sort()    # sort them in ascending way   1,2,3,....
print("After  Sorting: ",List)
# Revese the list 
List.reverse() #  sorth them in decending way 3,2,1,....
print("After  Reverse: ",List)
# get the size of the list 
print("Size          : ",len(List))
print("\n============= Exercise5 =============\n")
#Exercise 5

students = ["Ahmed","Ashraf","Mohamed",["Ali","Hany","Fareed"]]
print(students[3][0],students[3][2],"\n")




