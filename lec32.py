# this lectures covers : Handling Exception  

'''
what is Exception? it is an error or a bug that happen in runtime (runtime error)

how to handle the Exception?
by using try :   except :

'''

print("============ Example1 ============")
x = 10
y = 0
try:
    print("Result ",x/y)
except Exception as e:
    print("Invalid Operation")
print("============ Example2 ============")
List = [1,2,3,4,5]
try:
    print(List[5])
except Exception as e:
    print("Out Of Range")
finally :
    print("You Handled it")
