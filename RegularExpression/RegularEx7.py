import re
pattern = r"\b\w+ing\b"
text = "Walking and Talking are important activities"
#match_result = re.search(pattern, text)
match_result = re.findall(pattern, text)
if match_result:
    #print("Match found : ", match_result.group())
    print("Match found : ", match_result)
else:
    print("Match not found.") 