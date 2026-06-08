class Myclass:
    x=5
    def display(self):
        print("I am inside the function")
obj = Myclass()
print('state : ', obj.x)
print("Behaviour : ")
obj.display()

class Myclass:
    def __init__(self, name):
        self.name = name
    def say_hi(self):
        print("Hello, my name is ", self.name)
obj = Myclass('shon')
obj.say_hi()

class Myclass:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say_hi(self):
        print("Hello,Good Morning ", self.name)
        print("What's your age is ", self.age)
obj = Myclass('Resh', 26)
obj.say_hi()