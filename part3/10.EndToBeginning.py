text = input("Please type in a string: ")

numOfChar = len(text) - 1
while numOfChar >= 0:
    print(text[numOfChar])
    numOfChar -= 1