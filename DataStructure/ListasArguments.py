def increment(list2):
    for i in range(0, len(list2)):
        list2[i] += 5
    print("Reference of list inside function ", id(list2))
list1 = [10, 20, 30, 40, 50]
print("Reference of list in main ",id(list1))
print("The list before the function call")
print(list1)
increment(list1)
print("The list after the function call")
print(list1)

#function to increment the elements of the list passed as arguments
def increment(list2):
    print("\nID of list inside function before assignment : ", id(list2))
    list2 = [1, 2, 3, 4, 5]
    for i in range(0, len(list2)):
        list2[i] += 5
    print("ID id list changes inside function after assignment : ", id(list2))
    print("The list inside the function after assignment is : ")
    print(list2)
list1 = [10, 20, 30, 40, 50]
print("Reference of list in main ",id(list1))
print("The list before the function call")
print(list1)
increment(list1)
print("The list after the function call")
print(list1)