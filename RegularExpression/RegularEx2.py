import re
text = '''Alan Turing was pioneer of theorectical computer science and artificial intelligence. He was born on 23 June 1912 in Madia Vale, London'''
res = re.search('Turing', text)
print(type(res))
print("Result = {}".format(res))
print("Result = {} and start, end position={}".format(res, res.span()))