list1 = [10, 15, 20, 25]
while True:
    print("Menu Driven")
    print("OPTIONS ARE LISTED OUT")
    print("1. Append an element")
    print("2. Insert an element")
    print("3. Append a list to the given list")
    print("4. Modify an existing element")
    print("5. Delete an existing element from its position")
    print("6. Delete an existing element with a given value")
    print("7. Sort the list in ascending order")
    print("8. Sort the list in descending order")
    print("9. Display the list")
    print("10. Exit")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        element = int(input("Enter the element : "))
        list1.append(element)
        print("The element append to the list : ",list1)
    elif choice == 2:
        element = int(input("Enter the element : "))
        pos = int(input("Enter position : "))
        list1.insert(pos, element)
        print("The element after insert : ", list1)
    elif choice == 3:
        list2 = eval(input("Enter the list : "))
        list1.extend(list2)
        print("The list after append : ", list1)
    elif choice == 4:
        pos = int(input("Enter position : "))
        element = int(input("Enter value : "))
        list1[pos] = element
        print("The modified list:", list1)
    elif choice == 5:
        pos = int(input("Enter position : "))
        list1.pop(pos)
        print("The list after delete an element from its poition : ",list1)
    elif choice == 6:
        element = int(input("Enter element : "))
        list1.remove(element)
        print("The list after delete the given value",list1)
    elif choice == 7:
        list1.sort()
        print("The sorted list : ", list1)
    elif choice == 8:
        list1.sort(reverse=True)
        print("The descending order of the list : ", list1)
    elif choice == 9:
        print(list1)
    elif choice == 10:
        break
    else:
        print("Invalid number")