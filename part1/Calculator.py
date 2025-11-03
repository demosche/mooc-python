num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
oper = input("Operation: ")

if oper == "add":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif oper == "multiply":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif oper == "subtract":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")