try:
    a = int(input())
    b = int(input())
    c = a/b
except(ZeroDivisionError):
    print("Can't divide with zero")
    print("Successfully Executed")

try:
    a = int(input())
    b = int(input())
    c = a/b
    print("a/b = ", c)
except(ZeroDivisionError):
    print("Can't divide with zero")
else:
    print("I will execute when no exception occurs")

try:
    a = int(input())
    b = int(input())
    c = a/b
    print("a/b = ", c)
except NameError:
    print("This is value error")
except Exception:
    print("Can't divide with zero")
    print(Exception)
else:
    print("I will execute when no exception occurs")


try:
    a = int(input())
    b = int(input())
    c = a/b
    print("a/b = ", c)
except ZeroDivisionError:
    print("Can't divide with zero")
else:
    print("I will execute when no exception occurs")
finally:
    print("I am always Executing")