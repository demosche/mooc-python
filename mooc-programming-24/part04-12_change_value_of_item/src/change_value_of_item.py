numbers = [1, 2, 3, 4, 5]

while True:
    index = int(input("Index: "))
    
    if index == -1:
        break
    
    newP = int(input("New value: "))
    numbers[index] = newP
    print(numbers)