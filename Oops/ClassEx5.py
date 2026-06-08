class Student:
    def __init__(self):
        self.name = 'janani' #public
        self.__age = 21 #private
obj = Student() #object creation
print(obj.name) #calling using obj.ref of student class - NoError
print(obj.__age) #throws an error