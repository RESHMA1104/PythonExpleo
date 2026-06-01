marks = int(input())
if marks > 90:
    print("O")
elif marks > 81 and marks <= 90:
    print("A")
elif marks > 71 and marks <= 80:
    print("B")
elif marks > 61 and marks <= 70:
    print("C")
elif marks >= 50 and marks <= 60:
    print("D")
elif marks < 50:
    print("F")
