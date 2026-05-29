def line(length, charString):
    if len(charString) == 0:
        char = "*"
    else:
        char = charString[0]
    
    print(char * length)

def box_of_hashes(height):
    for i in range(height):
        line(10, "#")

if __name__ == "__main__":
    box_of_hashes(5)
    print()
    box_of_hashes(2)