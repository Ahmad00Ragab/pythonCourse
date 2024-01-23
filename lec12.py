# this lec covers :  Lists 

'''
list is a set of elements, these elements can be of different types 
it is declared like this :
list = [ele1,ele2,ele3,ele4]
notice that : ele1 , ele2 ,… are of different types 
methods that are applied on the list:
list.sort()               ==> sort the list
list.append(number)       ==> add a new number in the end of the list 
len(list)                 ==> get the size of the length
min(list)                 ==> get the min number of the list 
max(list)                 ==> get the max number of the list 
list.reverse()            ==> revser the list
list.count(number)        ==> count the number of occurence of the input number in the list 
list.extend(list)         ==> add a new list at the end of the list 
list.insert(index,number) ==> insert a new number in the index specified in the list
list.index(number)        ==> get the index of the passed number and if it doesn't exist
                              it makes an error in the program 
list.pop()                ==> get the last element of the list and remove it 
list.remove(number)       ==> remove the specified element in the list 
list.clear()              ==> remove all elements from the list and make it empty 

# copying the lists : 
method1:
newList = oldList 
method2:
newList = list(oldList)
method3:
newList = oldList.copy()

# adding two lists 
  +  : merging two list 
  newList = oldList1 + oldList2
'''
# declaring and initializing a list
Numbers = [5,6,9,7,1,30,56,9,9]

#displaying the list 
print(Numbers)
# print the min number of elements in the list 
print ("Min : ",min(Numbers))
# print the min number of elements in the list 
print ("Max : ",max(Numbers))
# print the min number of elements in the list 
print ("Len : ",len(Numbers))
#sorting the list 
Numbers.sort()
#display the list after sorting 
print(Numbers)
# reverse the list 
Numbers.reverse()
# displying the list after reversing it 
print(Numbers)
# append a new number 
Numbers.append(15)
# displying the list after appending 15  
print(Numbers)
# count the number of occurence of number 9 in the list  
print(Numbers.count(9))

# add a new list to the existed list 
Numbers2 = [100,200,300]
Numbers.extend(Numbers2)
#display the new Numbers list 
print(Numbers)
# insert a new number in the list at the specified index 
Numbers.insert(len(Numbers),400)
# display the new Numbers list 
print(Numbers)
# get the index of a number
print(Numbers.index(400))
# if the number is exist 
# print(Numbers.index(1000)) # error 
# pop the last element of the list 
print (Numbers.pop())
#remove the last element of the list 
Numbers.remove(300)
# display the list after removing the last element 
print(Numbers)
# clear the list 
Numbers.clear()
# display the empty list 
print(Numbers)
# copy an existing list to a new list 
Numbers3 = Numbers2

# copying list #
Numbers2 = [100,200,300,400,500]
# method1
newList1  = Numbers2
print(newList1)
#method2 
newList2 = list(Numbers2)
print(newList2)
#method3
newList3 = Numbers2.copy()
print(newList3)

# there is a difference between  method1  and the other two methods #
# method 1 is copy by reference which means that any modification happens 
# in the original list, make changes in the copied list, 
# in the other two methods , it is pass by value

# make a change in the original list
Numbers2.append(600)

# display the lists
print(newList1)
print(newList2)
print(newList3)

# merging list using + operator
Numbers.append(10)
Numbers.append(20)
Numbers.append(30)
new_List = Numbers + Numbers2

# display the new list 
print(new_List)





