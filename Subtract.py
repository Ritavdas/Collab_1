def subtract(num1, num2):
    if num1 >= num2:
        return num1 - num2
    else:
        return num2 - num1


a = int(input("Enter one Number: "))
b = int((input("Enter second Number: ")))

print(subtract(a, b))

subtract_result = subtract(a, b)
print(f'Result of subtraction of {a} and {b} =  {subtract_result}')
