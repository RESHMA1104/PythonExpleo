my_tuple = 10
print(type(my_tuple))
my_tuple = (10, 20)
print(type(my_tuple))
my_tuple = 10,
print(type(my_tuple))
my_tuple = (10, 3.14, "ram", [1, 2, 3, 0.4, 2.6])
print(type(my_tuple))
print(type(my_tuple[3]))
print(type(my_tuple[3][3]))

t = (10, 20, 30, 40, 50)
t = (100,) + t[1:]
print(t)

addr = "monty@python/org"
uname, domain = addr.split('@')
print(uname)
print(domain)
print(type(addr))

quot, rem = divmod(7, 3)
print(quot)
print(rem)

#Dictionary
my_dict = {}
my_dict = {1 : "Apple", 2 : "Ball"}
print(type(my_dict))
dict3={1:"CSE",'name':"sam",'list':[1,2,3],'tuple':(1,2,3)}
print(type(dict3))
print(dict())

print(dict())
numbers = dict(x=5, y=0 )

num2=dict({'x':4,'y':5})
print(num2)

num3=dict([('x',4),('y',5)])
print(num3)

Myfam={"child1":{"name":"ram","age":11},"child2":{"name":"ramya","age":14}}
print(Myfam)
print(Myfam["child2"])
print(Myfam["child1"]["name"])

dict = {'name':'Arul Kumar', 'age':35, 'mail' : 'arul@gmail.com'}
print(dict['age'])
print(dict['name'])

thisdict = {'brand':'Ford', 'model':'Mustang', 'year': 1964}
print(thisdict)
#del thisdict['model']
for x in thisdict:
    print(x, thisdict[x])

d = {1 : 'one', 2 : 'two', 3 : 'three', 4 : 'Four'}
print(d.keys())
print(d.values())
print(d.items())
#print(d.clear())
print(d.pop(1))
print(d)
print(d.popitem())
print(d)
print(d.get(2, "Not Found"))
print(d.copy())
d1 = {2 : 'Four'}
d.update(d1)
print(d)

square = {x : x*x for x in range(5) }
print(square)

square = {x : x*x for x in range(10) if x % 2 == 1 }
print(square)

#Set
my_set = {1, 2, 3, 4, 3, 2}
print(my_set)
#my_set1 = {[1, 2, 3, 2]}
#print(my_set1)
#my_set2 = {1, 2, [3, 4]}
#print(my_set2)
my_set2 = {1, 2, (3, 4)}
print(my_set2)
my_set.add(5)
print(my_set)
my_set.update([6, 7, 8])
print(my_set)
my_set.discard(4)
print(my_set)
my_set.discard(9)
print(my_set)
my_set.remove(6)
print(my_set)
#my_set.remove(10)
#print(my_set)
my_set.pop() # removes the first element
print(my_set)
my_set.pop()
print(my_set)

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}