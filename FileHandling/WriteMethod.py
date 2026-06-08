my_obj=open("Myfiles.txt","w")
my_obj.write("Heyy!! I have Started learning Python\n")
my_obj.write(str(58)) # we i have to type cast otherwise it shows error

myObject = open("test.txt", "w")
lines = ["Hello everyone\n", "Writing #multiline strings\n", "This is the #third line"]
myObject.writelines(lines)
#myObject.close()