def same_chars(string, i1, i2):
    if i1 < 0 or i1 >= len(string) or i2 < 0 or i2 >= len(string):
        return False
    
    return string[i1] == string[i2]


if __name__ == "__main__":
    print(same_chars("programmer", 6, 7))
    
    print(same_chars("programmer", 0, 4))
    
    print(same_chars("programmer", 0, 12))
    
    print(same_chars("hello", 0, 0))
    print(same_chars("hello", 0, 2))
    print(same_chars("hello", -1, 2))
    print(same_chars("hello", 0, 10))