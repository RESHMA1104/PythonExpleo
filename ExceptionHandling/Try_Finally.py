try:
    #fh = open("test.txt", "w")
    fh = open("testpath\.txt", "w")
    try:
        fh.write("This is my file for exception handling!!")
    finally:
        print("Going to close the file")
        fh.close()
except IOError:
    print("Error: can't find file to write data")
else:
    print("I will execute when no exception occurs")
finally:
    print("I am always executing")



try:
    num = int(input("Enter the positive integer : "))
    #if(num <= 0):
        #raise ValueError("This is negative number")
except ValueError as e:
    print(e)
print("I am successfully handled")