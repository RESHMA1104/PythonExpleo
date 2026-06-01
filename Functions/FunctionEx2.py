def Circle(radius):
    print("Area of circle", 3.14 * radius * radius)

def Rectangle(length, breadth):
    print("Area of rectangle", length * breadth)

def Square(side):
    print("Area of square", side * side)

while True:
    print("Menu Driven")
    print("1. Area of circle")
    print("2. Area of Rectangle")
    print("3. Area of Square")
    print("4. Exit")

    choice = int(input("Enter the choice : "))

    if choice == 1:
        r = int(input("Enter the radius : "))
        Circle(r)

    elif choice == 2:
        length = int(input("Enter the length : "))
        b = int(input("Enter the breadth : "))
        Rectangle(length, b)

    elif choice == 3:
        s = int(input("Enter the side : "))
        Square(s)

    elif choice == 4:
        break

    else:
        print("Wrong choice")