print("Person 1:")
firName = input("Name: ")
age1 = int(input("Age: "))

print("Person 2:")
secName = input("Name: ")
age2 = int(input("Age: "))

if age1 > age2:
    print(f"The elder is {firName}")
elif age2 > age1:
    print(f"The elder is {secName}")
else:
    print(f"{firName} and {secName} are the same age")