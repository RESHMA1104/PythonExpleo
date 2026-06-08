def add_mul(num1, num2, num3):
    out = (num1+num2)*num3
    return out
input1 = int(input("Enter the first integer : "))
input2 = int(input("Enter the second integer : "))
input3 = int(input("Enter the third integer : "))
result = add_mul(input1, input2, input3)
print(result)