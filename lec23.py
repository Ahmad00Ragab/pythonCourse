# this lec covers :  Break, Continue    

''' 
break and continue both of are keyword that are used with loops 

Break    : break the loop that you are in it now 
continue : tell the program go to the next iteration directly without executing
           the following lines of code
'''

students = ["Paul","Erin","Connie","Moira",]

for i in range(len(students)):
   
    if(i == 2):
        continue
    else:
        print(students[i])
        print("Counter is : ",i)

print("Program is complete")