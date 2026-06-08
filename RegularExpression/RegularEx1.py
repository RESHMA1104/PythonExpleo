import re
text = '''Alan Turing was pioneer of theorectical computer science and artificial intelligence. He was born on 23 June 1912 in Madia Vale, London'''
res = re.findall('Turing', text) #even if i give aTuringb it will find Turing and print it
res1 = re.findall('was', text)
print(type(res))
print("Result = {}".format(res))
print("Result = {}".format(res1))