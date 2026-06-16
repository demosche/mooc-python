def greatest_number(x, y, z):
    if x >= y and x >= z:
        return x
    elif y >= x and y >= z:
        return y
    else:
        return z


if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)
    
    print(greatest_number(3, 7, 2))
    print(greatest_number(10, 10, 10))
    print(greatest_number(-5, -2, -8))