#Type Error
def add_mul(num1, num2, num3):
    out = (num1+num2) * num3
    return out
#input1 = str(input("Enter the first Integer : "))
input1 = int(input("Enter the first Integer : "))
input2 = float(input("Enter the second Integer : "))
result = add_mul(input1, input2) #It should match the given arguments
print(result)