# this lec covers : Functions Part2 

'''
difference between argument and parameter :
we have function definition and funcation calling 
s
in function definition ==> 
def fun(para1,para2):  para1 amd para2 are called parameters

In function calling ==>   
fun(arg1,arg2)      : arg1 and arg2 are called arguments 

4 types of function arguments or 4 methods that we can call the function with:

# method1 (required arguments)
fun(argument1,argument2)

#method2  (Keyword arguments)
fun(argument1 = 'value', argument2 = 'value')

#method3  (default arguments)
fun(argument1) # here in the definition, there should be a default value for the other aguments 

#method4  (variable length arguments)
fun(any_number_of_arguments)  # in the definintion ==> def fun(*parameter): 

( *parameter ) :  means that this function can receive any number of parameters 

'''

# method1,2
def add1(name,age):
    print("Hello, ",name," ",age)

#method3
def add2(name,age=28):
    print("Hello, ",name," ",age)

#method4
def add3(*name):
    for i in name:
        print("Hello, !",i)

# calling the function 
# method1
add1("Ahmad",'28')
# method2
add1(age= '28',name= 'Ahmad')
# method3
add2('Ahmad')
# method4
add3('Ahmad','Ali','Amr','Karim')

