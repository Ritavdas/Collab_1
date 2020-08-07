a = int(input("Enter one Number: "))
b = int((input("Enter second Number: ")))


def add(num1, num2):
    return num1 + num2


print(add(a, b))

add_result = add(a, b)
print(f'Result of addition of {a} and {b} =  {add_result}')

def div(x,y):
    return x/y

print(div(a,b))

div_result = div(a,b)
print(f'Result of division of {a} and {b} =  {div_result}')
