word = input("Word: ")
otstup = "*" * 30
gap = 30 - len(word) - 2
left = gap // 2
right = gap - left
print(otstup)
print("*" + " " * left + word + " " * right + "*")
print(otstup)