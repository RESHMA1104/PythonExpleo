n = input("Enter String : ")
#if n.__eq__(n[::-1]):
if n==n[::-1]:
    print(n, "is palindrome string")
else:
    print(n, "is not a palindrome string")