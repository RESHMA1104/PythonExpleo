# To store a list using append
list1 = []
n = int(input("Enter the number of elements in the list : "))
for i in range(0, n):
    print("Enter element No-{}:".format(i+1)) #To mention the number of elements as 1,2,3....
    element = int(input())
    list1.append(element)
    print("The Elements in the list are ", list1)

#create a list using split
list2 = []
n = int(input("Enter the number of elements in the list : "))
list2 = input("Enter the list elements separated by comma : ").split()
print("The elements in the list are ", list2)

#create a list using split and map function
t = list(map(int, input("Enter the List elements :").split()))
print("Enter the number of elements : ", t)