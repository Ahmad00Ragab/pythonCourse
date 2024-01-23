# this lectures covers : MultiLevel inheritance  

'''
MultiLevel Inheritance : it is called mulitple inheritance and it is the process in which a new class inherits
two parent classes 
'''

class CollegeData:
    def __init__(self,name,CollegeId,age):
        self.name      = name
        self.CollegeId = CollegeId
        self.age       = age
    def displayCollegeData(self):
        print("CollegeId : ",self.CollegeId," Age: " ,self.age)    

class HostelData:
    def __init__(self,hostlelId,roomNumber):
        self.hostelId = hostlelId
        self.roomNumber = roomNumber
    
    def displayHostelData(self):
        print("HostelId : ",self.hostelId," RoomNumber: ",self.roomNumber)

class Student(CollegeData,HostelData):
    def __init__(self, name, CollegeId, age,hostlelId,roomNumber,grade):
        CollegeData.__init__(self,name,CollegeId,age)
        HostelData.__init__(self,hostlelId,roomNumber)
        self.grade = grade

# creating an object from Student Class
student1 = Student("Ahmad",'1','22','789','123','Good')

student1.displayCollegeData()
student1.displayHostelData()

