myobj = open("test.txt", "r")
#var = myobj.read(15)
#print(var)
#var = myobj.read(-7) #.read()
#print(var)
#myobj.close()

#print(myobj.readline())
#print(myobj.readlines())

d = myobj.readlines()
for line in d: #list iterable - d
    #words = line.split() #used split() function
    words = line.splitlines()
    print(words)