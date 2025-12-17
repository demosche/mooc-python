limit = int(input("Limit: "))
total = 0
number = 1
numbers = ""

while total < limit:
    total += number
    if numbers == "":
        numbers = str(number)
    else:
        numbers += " + " + str(number)
    number += 1

print(f"The consecutive sum: {numbers} = {total}")