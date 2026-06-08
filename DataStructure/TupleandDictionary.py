my_tuple = 10
print(type(my_tuple))
my_tuple = (10, 20)
print(type(my_tuple))
my_tuple = 10,
print(type(my_tuple))
my_tuple = (10, 3.14, "ram", [1, 2, 3, 0.4, 2.6])
print(type(my_tuple))
print(type(my_tuple[3]))
print(type(my_tuple[3][3]))

t = (10, 20, 30, 40, 50)
t = (100,) + t[1:]
print(t)

addr = "monty@python/org"
uname, domain = addr.split('@')
print(uname)
print(domain)
print(type(addr))

quot, rem = divmod(7, 3)
print(quot)
print(rem)

#Dictionary
my_dict = {}
my_dict = {1 : "Apple", 2 : "Ball"}
print(type(my_dict))
dict3={1:"CSE",'name':"sam",'list':[1,2,3],'tuple':(1,2,3)}
print(type(dict3))
print(dict())

print(dict())
numbers = dict(x=5, y=0 )

num2=dict({'x':4,'y':5})
print(num2)

num3=dict([('x',4),('y',5)])
print(num3)

Myfam={"child1":{"name":"ram","age":11},"child2":{"name":"ramya","age":14}}
print(Myfam)
print(Myfam["child2"])
print(Myfam["child1"]["name"])

dict = {'name':'Arul Kumar', 'age':35, 'mail' : 'arul@gmail.com'}
print(dict['age'])
print(dict['name'])

thisdict = {'brand':'Ford', 'model':'Mustang', 'year': 1964}
print(thisdict)
#del thisdict['model']
for x in thisdict:
    print(x, thisdict[x])

d = {1 : 'one', 2 : 'two', 3 : 'three', 4 : 'Four'}
print(d.keys())
print(d.values())
print(d.items())
#print(d.clear())
print(d.pop(1))
print(d)
print(d.popitem())
print(d)
print(d.get(2, "Not Found"))
print(d.copy())
d1 = {2 : 'Four'}
d.update(d1)
print(d)

square = {x : x*x for x in range(5) }
print(square)

square = {x : x*x for x in range(10) if x % 2 == 1 }
print(square)

#Set
my_set = {1, 2, 3, 4, 3, 2}
print(my_set)
#my_set1 = {[1, 2, 3, 2]}
#print(my_set1)
#my_set2 = {1, 2, [3, 4]}
#print(my_set2)
my_set2 = {1, 2, (3, 4)}
print(my_set2)
my_set.add(5)
print(my_set)
my_set.update([6, 7, 8])
print(my_set)
my_set.discard(4)
print(my_set)
my_set.discard(9)
print(my_set)
my_set.remove(6)
print(my_set)
#my_set.remove(10)
#print(my_set)
my_set.pop() # removes the first element
print(my_set)
my_set.pop()
print(my_set)

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}




dict = {
    "25MCA001": 77,
    "25MCA025": 99,
    "25MCA012": 84,
    "25MCA032": 83,
    "25MCA009": 60,
    "25MCA007": 84,
    "25MCA021": 86,
    "25MCA018": 40,
    "25MCA014": 40
}

distinction = 0
merit = 0
passed = 0
fail = 0

total = 0

print("STUDENT RESULT")

for key, val in dict.items():

    if val >= 86 and val <= 100:
        print("Distinction :", key, val)
        distinction += 1

    elif val >= 76 and val <= 85:
        print("Merit :", key, val)
        merit += 1

    elif val >= 60 and val <= 75:
        print("Pass :", key, val)
        passed += 1

    else:
        print("Fail :", key, val)
        fail += 1

    total = total + val

# Maximum mark
max_mark = max(dict.values())

for key, val in dict.items():
    if val == max_mark:
        print("Maximum :", key, val)

# Minimum mark
min_mark = min(dict.values())

for key, val in dict.items():
    if val == min_mark:
        print("Minimum :", key, val)

# Average
avg = total / len(dict)

print("Average :", avg)

# Count
print("Distinction Count :", distinction)
print("Merit Count :", merit)
print("Pass Count :", passed)
print("Fail Count :", fail)

# Leaderboard
print("Leaderboard")

leaderboard = sorted(dict.items(), key=lambda x: x[1], reverse=True)

for key, val in leaderboard:
    print(key, val)



dict = {
    "25MCA001": 77,
    "25MCA009": 60,
    "25MCA025": 99,
    "25MCA007": 84,
    "25MCA012": 45,
    "25MCA021": 86,
    "25MCA032": 83,
    "25MCA018": 40,
    "25MCA014": 67
}

distinction = []
merit = []
passed = []
fail = []

total = 0

# Classification
for key, val in dict.items():

    total = total + val

    if val >= 86 and val <= 100:
        distinction.append(key)

    elif val >= 76 and val <= 85:
        merit.append(key)

    elif val >= 60 and val <= 75:
        passed.append(key)

    else:
        fail.append(key)

# Maximum
max_mark = max(dict.values())

for key, val in dict.items():
    if val == max_mark:
        print("Maximum:", val, "—", key)

# Minimum
min_mark = min(dict.values())

for key, val in dict.items():
    if val == min_mark:
        print("Minimum:", val, "—", key)
        break

# Distinction
print("Distinction:", len(distinction), "→", distinction)

# Merit
print("Merit:", len(merit), "→", merit)

# Pass and Fail count
print("Pass:", len(passed), "| Fail:", len(fail))

# Average
avg = total / len(dict)

print("Class Average:", round(avg, 2))

# Below Average Students
below_avg = []

for key, val in dict.items():
    if val < avg:
        below_avg.append(key)

print("Below Avg:", below_avg)

# Leaderboard
print("--- Leaderboard ---")

leaderboard = sorted(dict.items(), key=lambda x: x[1], reverse=True)

for key, val in leaderboard:
    print(key, ":", val)



class Person:

    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def display_info(self):
        print("Name :", self.name)
        print("Age :", self.age)
        print("Email :", self.email)


class Trainee(Person):

    def __init__(self, name, age, email, batch_id, marks, num_projects, num_publications):
        Person.__init__(self, name, age, email)

        self.batch_id = batch_id
        self.marks = marks
        self.num_projects = num_projects
        self.num_publications = num_publications

    def display_info(self):
        Person.display_info(self)

        print("Batch :", self.batch_id)
        print("Marks :", self.marks)
        print("Projects :", self.num_projects)
        print("Publications :", self.num_publications)


class SDETTrainee(Trainee):

    def __init__(self, name, age, email, batch_id, marks,
                 num_projects, num_publications, tool_proficiency):

        Trainee.__init__(self, name, age, email, batch_id,
                         marks, num_projects, num_publications)

        self.tool_proficiency = tool_proficiency

    def compute_aggregate(self):

        avg_marks = sum(self.marks) / len(self.marks)

        aggregate = (avg_marks * 0.6) + \
                    (self.num_projects * 5) + \
                    (self.num_publications * 3)

        return aggregate

    def display_info(self):

        Trainee.display_info(self)

        avg_marks = sum(self.marks) / len(self.marks)

        print("Tool :", self.tool_proficiency)

        print("Average Marks :", round(avg_marks, 2))

        aggregate = self.compute_aggregate()

        print("Aggregate Score :", round(aggregate, 2))

        print()

        print(round(avg_marks, 2), "× 0.6 =",
              round(avg_marks * 0.6, 2))

        print(self.num_projects, "× 5 =",
              self.num_projects * 5)

        print(self.num_publications, "× 3 =",
              self.num_publications * 3)

        print("----------------------")

        print("Total =", round(aggregate, 2))


# Object list
trainees = []

# Input for 2 trainees
for i in range(2):

    print("\nEnter Trainee", i + 1, "Details")

    name = input("Enter Name : ")
    age = int(input("Enter Age : "))
    email = input("Enter Email : ")

    batch_id = input("Enter Batch ID : ")

    marks = []

    for j in range(5):
        mark = int(input("Enter Subject Mark : "))
        marks.append(mark)

    num_projects = int(input("Enter Number of Projects : "))
    num_publications = int(input("Enter Number of Publications : "))

    tool_proficiency = input("Enter Tool Proficiency : ")

    obj = SDETTrainee(name, age, email, batch_id,
                      marks, num_projects,
                      num_publications, tool_proficiency)

    trainees.append(obj)

# Display Details
print("\n----- TRAINEE DETAILS -----")

for t in trainees:
    t.display_info()
    print()

# Highest Aggregate
highest = trainees[0]

for t in trainees:
    if t.compute_aggregate() > highest.compute_aggregate():
        highest = t

print("----- HIGHEST AGGREGATE -----")

print("Name :", highest.name)
print("Aggregate Score :", round(highest.compute_aggregate(), 2))


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

    def __init__(self, name, age, email, batchid,
                 marks, proj, publication, tool_profi):

        Trainee.__init__(self, name, age, email,
                          batchid, marks, proj, publication)

        self.tool_profi = tool_profi

    def compute_agg(self):

        avg_marks = sum(self.marks)/len(self.marks)

        agg = (avg_marks * 0.6) +  \
              (self.proj * 5) +  \
              (self.publication * 3)

        return agg


# Object Creation
obj1 = SDETrainee(
    "Arun", 24, "arun@gmail.com",
    "B2025",
    [78, 85, 90, 72, 88],
    3,
    1,
    "Selenium"
)

# Printing
obj1.dis_info()

print("Tool : ", obj1.tool_profi)

avg = sum(obj1.marks)/len(obj1.marks)

print("Average Marks : ", avg)

print("Aggregate Score : ", obj1.compute_agg())



import re

try:

    file = open("server_log.txt", "r")

    data = file.read()

    file.seek(0)

    lines = file.readlines()

    # Count lines
    total_lines = len(lines)

    # Count words
    total_words = len(data.split())

    # Count characters
    total_chars = len(data)

    # Count vowels
    vowels = "aeiouAEIOU"

    total_vowels = 0

    for ch in data:
        if ch in vowels:
            total_vowels += 1

    # Regex for log levels
    info = len(re.findall(r"\[INFO\]", data))

    warning = len(re.findall(r"\[WARNING\]", data))

    error = len(re.findall(r"\[ERROR\]", data))

    critical = len(re.findall(r"\[CRITICAL\]", data))

    # Alert Summary
    alerts = []

    for line in lines:

        if "ERROR" in line or "CRITICAL" in line:
            alerts.append(line.strip())

    # Write into report file
    report = open("log_report.txt", "w")

    report.write("Total Lines : " + str(total_lines) + "\n")

    report.write("Total Words : " + str(total_words) + "\n")

    report.write("Total Chars : " + str(total_chars) + "\n")

    report.write("Total Vowels : " + str(total_vowels) + "\n\n")

    report.write("INFO : " + str(info) + "\n")

    report.write("WARNING : " + str(warning) + "\n")

    report.write("ERROR : " + str(error) + "\n")

    report.write("CRITICAL : " + str(critical) + "\n\n")

    report.write("--- ALERTS ---\n")

    for i in alerts:
        report.write(i + "\n")

    print("Report Generated Successfully")

except FileNotFoundError:

    print("File not found")

except Exception as e:

    print("Error :", e)

finally:

    try:
        file.close()
        report.close()

    except:
        pass