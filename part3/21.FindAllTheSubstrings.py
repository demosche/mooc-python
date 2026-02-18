word = input("Please type in a word: ")
char = input("Please type in a character: ")

start = 0
while start < len(word):
    if word[start] == char and start <= len(word) - 3:
        print(word[start:start+3])
    start += 1