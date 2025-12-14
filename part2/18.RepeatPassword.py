passw = input("Password: ")

while True:
    denied_pass = input("Repeat password: ")

    if denied_pass == passw:
        print("User account created!")
        break
    else:
        print("They do not match!")