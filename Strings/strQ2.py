input1 = input("Enter the string : ")
substring = input("Enter the substring : ")
pos = input1.rfind(substring)
if(pos != -1):
    print("Last occurence of ", substring, " starts at index ", pos)