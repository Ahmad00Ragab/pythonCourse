# this lec covers :  Dictionaries

'''
dict : dictionary is on the following format ==> dict = {key1:value1, key2:value2}
restrictions: 
1. keys must be unique 
2. keys can't be changed (immutable)

there are 4 methods to define a dictionary 
1. dict = {key1:vlaue1, key2:value2}          # dict 
2. dict = dict([(key1,vlaue1),(key2,value2)]) # list of tuples casted to dict
3. dict = dict(key1=value1,key2=value2)       # tuples casted to dict
4. dict = dict({key1:value1, key2:value2}     # dict is casted to dict 

# Exercise 
Create a dictionary : Dictionary = {"Java":"95%","python" : "90%"} 
output              : "Java":"70%", "python":"80%"

'''

dict = {
    1  : "JAN",
    2  : "FEB",
    3  : "MAR",
    4  : "APR",
    5  : "MAY",
    6  : "JUN",
    7  : "JUL",
    8  : "AUG",
    9  : "SEP",
    10 : "OCT",
    11 : "NOV",
    12 : "DEC"
}

# accessing the dictionary elements
print(dict.get(1))
print(dict.get(12))
print(dict.get(13))

#Exercise 
Dictionary = {"Java":"95%","python" : "90%"} 
print(Dictionary)
Dictionary["Java"]   = "70"
Dictionary["python"] = "80"
print(Dictionary)