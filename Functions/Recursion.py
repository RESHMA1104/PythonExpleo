def factorial(num):
    if num==0:
        return 1
    else:
        return(num*factorial(num-1))
val1=int(input("Enter the number:"))
fact=factorial(val1)
print(fact)