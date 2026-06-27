count = int(input("How many items: "))
items = []

for i in range(1, count + 1):
    value = int(input(f"Item {i}: "))
    items.append(value)

print(items)