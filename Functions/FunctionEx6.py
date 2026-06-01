def add_mul(num1, num2, num3 = 6):
#def add_mul(num1 = 6, num2, num3): # If I gave Default parmater that following also should be default
    out = (num1+num2) * num3
    return out
input1 = int(input("Enter the first Integer : "))
input2 = int(input("Enter the second Integer : "))
result = add_mul(input1, input2) #It should match the given arguments
print(result)