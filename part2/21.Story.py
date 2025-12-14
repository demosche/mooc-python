words = []

while True:
    word = input("Please type in a word: ")

    if word == "end" or (words and word == words[-1]):
        break

    words.append(word)

print(" ".join(words))