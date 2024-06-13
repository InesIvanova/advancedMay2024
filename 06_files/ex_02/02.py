path = "numbers.txt"

total = 0
try:
    file = open(path, "r")
    lines = file.readlines()
    for line in lines:
        number = int(line[:-1])
        total += number
    print(total)
except FileNotFoundError:
    print("File not found")

