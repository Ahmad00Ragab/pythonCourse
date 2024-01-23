# this lec covers :  tuples

'''
tuple is a data structure that is defined using (), amd once it is identified, it is immutable
the elements inside the tuple could be of different data types 

operations on Tuple :
Access                       : accessed using index 
modification                 : tuple (calculation) 
Delete                       : del tuple
Tuple operators              : +,*
Tuple index and interception : [index]

Methods:
cmp(tuple1,tuple2)           ==> compare between two tuples
min(tuple)                   ==> get the min number of the tuple
max(tuple)                   ==> get the max number of the tuple
                             ==> 

Exercise1:

Create a tuple with 1,2,3 and another with A,B,C then
concatenate them together and print the new tuple 

'''

# define a Tuple
Tuple = (100,200,300,400)
# display the Tuple 
print(Tuple)
print(min(Tuple))
print(max(Tuple))

print("============ Exercise 1 =============")
Tuple1 = (1,2,3)
Tuple2 = ('A','B','C')
#concatenat eh two Tuples : Tuple1 , Tuple2
Tuple3 = Tuple1 + Tuple2
# display the result 
print(Tuple3)
#############################################
