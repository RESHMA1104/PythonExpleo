import re
text = "Alan Turing was born on 23 June 1912 in London. Long and Lonal"
res = re.findall("\\AAlan", text)
print("Result for \\A = ", res)
print("-"*79)

res = re.findall("\\bLon", text)
print("Result for \\b = ", res)
print("-"*79)

res = re.findall("\\Bon", text)
print("Result for \\B = ", res)
print("-"*79)

res = re.findall("\\d", text)
print("Result for \\d = ", res)
print("-"*79)

res = re.findall("\\D", text)
print("Result for \\D = ", res)
print("-"*79)

res = re.findall("\\s", text)
print("Result for \\s = ", res)
print("-"*79)

res = re.findall("\\S", text)
print("Result for \\S = ", res)
print("-"*79)

res = re.findall("\\w", text)
print("Result for \\w = ", res)
print("-"*79)

res = re.findall("\\W", text)
print("Result for \\W = ", res)
print("-"*79)

res = re.findall("Lonal\Z", text)
print("Result for \Z = ", res)