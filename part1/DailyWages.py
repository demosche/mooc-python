hourly = float(input("Hourly wage: "))
work = float(input("Hours worked: "))
day = input("Day of the week: ")

if day == "Sunday":
    d_wages = hourly * 2 * work
else:
    d_wages = hourly * work

print(f"Daily wages: {d_wages} euros")
