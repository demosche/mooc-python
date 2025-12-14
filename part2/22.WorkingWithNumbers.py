print("Please type in integer numbers. Type in 0 to finish.")

a = 0
b = 0
c = 0
d = 0

while True:
    e = int(input("Number: "))

    if e == 0:
        break

    a += 1
    b += e

    if e > 0:
        c += 1
    else:
        d += 1

print(f"Numbers typed in {a}")

if a > 0:
    print(f"The sum of the numbers is {b}")
    f = b / a
    print(f"The mean of the numbers is {f}")
    print(f"Positive numbers {c}")
    print(f"Negative numbers {d}")