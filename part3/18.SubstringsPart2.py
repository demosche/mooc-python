string = input("Please type in a string: ")

length = len(string)
for i in range(length):
    print(string[length - 1 - i:length])