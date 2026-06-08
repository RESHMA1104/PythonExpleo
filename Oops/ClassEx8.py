class Student:
    def getStudentInfo(self):
        self.__rollno = input("Enter Roll Number : ")
        self.__name = input("Enter Name : ")
    def printStudentInfo(self):
        print("Roll Number : ", self.__rollno)
        print("Name : ", self.__name)
class Marks(Student):
    def getmarks(self):
        self.getStudentInfo()
        self.__marks1 = float(input("Enter marks for subject1 : "))
        self.__marks2 = float(input("Enter marks for subject2 : "))
        self.__marks3 = float(input("Enter marks for subject3 : "))
    def printMarks(self):
        self.printStudentInfo()
        print("Marks1 : ", self.__marks1)
        print("Marks2 : ", self.__marks2)
        print("Marks3 : ", self.__marks3)