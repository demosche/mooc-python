def same_chars(str, FirC, SecC):
    if FirC < 0 or FirC >= len(str) or SecC < 0 or SecC >= len(str):
        return False
    return str[FirC] == str[SecC]

if __name__ == "__main__":
    print(same_chars("coder", 1, 2))