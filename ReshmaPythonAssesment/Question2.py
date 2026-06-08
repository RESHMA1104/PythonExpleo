class Person :
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
    def dis_info(self):
        print("Name : ", self.name)
        print("Age : ", self.age)
        print("Email : ", self.email)

class Trainee(Person):
    def __init__(self, name, age, email, batchid, marks, proj, publication):
        Person.__init__(self, name, age, email)
        self.batchid = batchid
        self.marks = marks
        self.proj = proj
        self.publication = publication
    def dis_info(self):
        Person.dis_info(self)
        print("Batch ID : ", self.batchid)
        print("Marks : ", self.marks)
        print("Project : ", self.proj)
        print("Publication : ", self.publication)

class SDETrainee(Trainee):
    def __init__(self, name, age, email, batchid, marks, proj, publication, tool_profi):
        Trainee.__init__(self, name, age, email, batchid, marks, proj, publication)
        self.tool_profi = tool_profi
    def  compute_agg(self):
        avg_marks = sum(self.marks)/len(self.marks)
        agg = (avg_marks * 0.6) +  (self.proj * 5) +  (self.publication * 3)
        return agg

obj1 = SDETrainee('Resh', 20, "resh@gmail.com", "B2025", [90, 70, 69, 85, 60], 3, 1, "Selenium")
obj1.dis_info()
print("Tool : ", obj1.tool_profi)
print("Aggregate Score : ", obj1.compute_agg)