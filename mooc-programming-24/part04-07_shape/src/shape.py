def line(length, char):
    """Prints a line of the given character with the specified length"""
    print(char * length)

def triangle(size, char):
    """Prints a triangle of given size using the specified character"""
    for i in range(1, size + 1):
        line(i, char)

def rectangle(width, height, char):
    """Prints a rectangle of given width and height using the specified character"""
    for i in range(height):
        line(width, char)

def shape(triHei, triChar, recHei, recChar):
    """Prints a triangle followed by a rectangle below it"""
    triangle(triHei, triChar)
    rectangle(triHei, recHei, recChar)

if __name__ == "__main__":
    shape(5, "x", 2, "o")