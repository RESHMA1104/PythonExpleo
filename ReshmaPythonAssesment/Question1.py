dict = {"25MCA001":77, "25MCA025":99, "25MCA012":45, "25MCA032":83, "25MCA009":60, "25MCA007":84, "25MCA021":86, "25MCA018":40, "25MCA014":67}
dist = []
pas = []
fail = []
merit = []
for key, val in dict.items():
    if val>=86 and val<=100:
        dist.append(key)

    elif val>=76 and val<=85:
        merit.append(key)

    elif val>=60 and val<=75:
        pas.append(key)

    else:
       fail.append(key)

maxx = max(dict.values())
for key, val in dict.items():
    if val == maxx:
        print("Maximum :", key, val)

minn = min(dict.values())
for key, val in dict.items():
    if val == minn:
        print("Minimum :", key, val)

print("Distinction : ",len(dist),dist)
print("Pass : ",len(pas), pas)
print("fail : ",len(fail), fail)
print("Merit : ", len(merit), merit)

bavg = []
print("Below Average")
for key, val in dict.items() :
    if val <= 60:
        bavg.append(key)
print(bavg)
        
ld = sorted(dict.items(), key=lambda x: x[1], reverse=True)
print("LeaderBoard")
for key, val in ld:
    print(key, ":", val)