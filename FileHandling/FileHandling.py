with open("test.txt", "r") as myObject:
    content = myObject.read()
    print(content)

with open("test.txt", 'w') as myobject:
    obj = myobject.write("Hey I have started using files in python\n")
    print(obj)

my_object=open("Myfiles3.txt","w")
sentence=input("Enter the Sentence:")
my_object.write(sentence)
my_object.close()
my_object=open("Myfiles3.txt","r")
for i in my_object:
    var=my_object.read()
    print(i)
my_object.close()