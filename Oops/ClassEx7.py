class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    def get_age(self):
        return self.__age
    def set_age(self, age):
        self.__age = age
student = Student('Mary', 14)
print('Name : ',    student.name,  student.get_age())
student.set_age(16)
print('Name : ',    student.name,  student.get_age())