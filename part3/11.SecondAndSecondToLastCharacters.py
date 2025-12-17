a = input("Please type in a string: ")

second = a[1]
secondEnd = a[-2]

if second == secondEnd:
    print(f"The second and the second to last characters are {second}")
else:
    print("The second and the second to last characters are different")