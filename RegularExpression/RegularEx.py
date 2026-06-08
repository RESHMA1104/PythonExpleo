import re
text = '''Alan Turing was pioneer of theorectical computer science and artificial intelligence. He was born on 23 June 1912 in Madia Vale, London'''
res = re.search("^Alan.*London$", text)
#res = re.search("^Alex.*London$", text)
print(type(res))
if(res):
    print("We have a match")
else:
    print("We don't have a match")