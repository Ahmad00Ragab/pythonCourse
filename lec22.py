# this lec covers :  Nested Loop   

''' 
nested loop : it is a loop inside a loop
'''

# defining a List of names 
List = ["Ahmad","Noor","Mourad","Raafat"]
# loop through the list and print each  name (as separated characters ) on a line  
# loop over name by name (i represents the name)
for i in List:
    # loop over each chracter from the current name 
    for char in i:
        print(f"{char} ",end="")
    print("") # print a new line 

print("============  ============")
# defining a list of lists 
List2 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for i in List2:
    for j in i:
        print(f"{j}  ",end ="")
    print("")

print("============  ============")
for i in range(0,3):
    for j in range(0,3):
        print(f"{List2[i][j]}  ",end="")
    print("")
