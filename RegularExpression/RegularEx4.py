import re
text = '''Alan Turing was pioneer of theoretical computer science and artificial intelligence. He was born on 23 June 1912 in Madia Vale, London'''
res = re.sub("theoretical", "practical", text)
print(type(res))
print("Result = {}".format(res))