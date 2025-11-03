students = int(input("How many students on the course? "))
groupsi = int(input("Desired group size? "))

groups = (students + groupsi - 1) // groupsi

print("Number of groups formed:", groups)
