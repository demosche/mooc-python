num = int(input("Please type in a number: "))

while num > 0:
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    print(f"The factorial of the number {num} is {fact}")
    num = int(input("Please type in a number: "))

print("Thanks and bye!")