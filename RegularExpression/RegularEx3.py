import re
text = '''Alan Turing was pioneer of theorectical computer science and artificial intelligence. He was born on 23 June 1912 in Madia Vale, London'''
res = re.split("a", text)
res1 = re.split("i", text)
print(type(res))
print("Result = {}".format(res))
print("Result = {}".format(res1))