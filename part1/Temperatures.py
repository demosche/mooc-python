FAH = float(input("Please type in a temperature (F): "))

cel = (FAH - 32) * 5 / 9

print(f"{FAH} degrees Fahrenheit equals {cel} degrees Celsius")

if cel < 0:
    print("Brr! It's cold in here!")
