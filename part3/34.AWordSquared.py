def squared(text, size):
    length = len(text)
    for i in range(size):
        row = ""
        for j in range(size):
            row += text[(i * size + j) % length]
        print(row)