def spruce(size):
    print("a spruce!")
    for i in range(size):
        print(" " * (size - i - 1) + "*" * (2 * i + 1))
    print(" " * (size - 1) + "*")

if __name__ == "__main__":
    spruce(5)