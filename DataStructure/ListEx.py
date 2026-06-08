t = list()
print(t)
print(type(t))
vowel_str = 'aeiou'
t = list(vowel_str)
print(t) 

t = [10, 20, 30, 40, 50]
del t[3]
print(t)
#del t
#print(t)

list1 = ['Red', 'Blue', 'Green', 'Pink', 'Yellow']
for i in range(len(list1)):
    print(list1[i])

list2 = ['Giraffee', 'Lion', 'Dog', 'Elephant', 'Cat']
list2.sort()
print(list2)
list2.sort(reverse = True)
print(list2)

list3 = [10, 40, 7, 39, 97, 28, 30]
list3.sort()
print(list3)
list3.sort(reverse=True)
print(list3)

list4 = [10, 40, 7, 39, 97, 28, 30]
list5 = sorted(list4)
print(list5)
print(max(list5))
print(min(list5))
print(sum(list5))

t = [1, 2, 3, 4, 5, 6, 7]
t1 = t.copy()
print(t1)
print(t)
t1[2] = 8
print(t1)
print(t.__eq__(t1))