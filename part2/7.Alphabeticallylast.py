slov = input("Please type in the 1st word: ")
word = input("Please type in the 2nd word: ")

if slov < word:
    print(f"{word} comes alphabetically last.")
elif slov > word:
    print(f"{slov} comes alphabetically last.")
else:
    print("You gave the same word twice.")