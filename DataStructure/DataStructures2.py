string="Good Day"
print(string[:7])
print(string[:-1])
print(string[1:2:1])
print(string[0:4:2])
print(string[::-1])
print(string[::-2])
str1="good"
str2="morning"
#using operators
print(str1+str2)
print(str1*3)
text="Hard Work never fails"
if "Work" in text:
    print("Yes")
else:
    print("No")
msg="Hello, World!"
new_msg='J'+msg[-6:-1]
print(new_msg)
word="Good Day"
Up=word.upper()
lo=word.lower()
print(Up)
print(lo)
index=word.find("a")
print(index)
index2=word.find("Da")
print(index2)
word2="banana"
index3=word2.find("na",3)
print(index3)
replace=word.replace("Good","Happy")
print(replace)
word3="Python Program"
counting=word3.count("o")
print(counting)
capital=word3.capitalize()
print(capital)
str3="sadar123"
print(str3.isalnum())#checks Alphabets and Numerics
str4="adjvk123"
print(str4.isalpha())
text2="Python is easy to learn"
print(text2.startswith("Python"))
print(text2.endswith("to"))
#reverse
word4="madam"
if word4==word4[::-1]:
    print(f"{word4} is a Palindrome")
else:
    print(f"{word4} is not a Palindrome")
# word5="wow"
# word6=word5[::-1]
# if word5.__eq__word6:
#     print(f"{word4} is a Palindrome")
# else:
#     print(f"{word4} is not a Palindrome")
string2=input("Enter a string:")
tot_num=0
tot_alpha=0
for i in string2:
    if i.isnumeric():
        tot_num+=1
    elif i.isalpha():
        tot_alpha+=1
    else:
        pass
print("Total Numbers found:",tot_num)
print("Total Letters found:",tot_alpha)