num = int(input("Please type in a number: "))

for f in range(1, num + 1):
    for l in range(1, num + 1):
        print(f"{f} x {l} = {f * l}")