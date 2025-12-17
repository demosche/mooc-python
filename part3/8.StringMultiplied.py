string = input("Please type in a string: ")
amount = int(input("Please type in an amount: "))

result = ""
counter = 0
while counter < amount:
    result += string
    counter += 1

print(result)