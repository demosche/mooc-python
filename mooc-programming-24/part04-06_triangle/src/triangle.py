# Copy here code of line function from previous exercise
def line(length, char):
    """Prints a line of the given character with the specified length"""
    print(char * length)

def triangle(size):
    for i in range(1, size + 1):
        line(i, "#")

if __name__ == "__main__":
    triangle(5)
    print()
    triangle(3)