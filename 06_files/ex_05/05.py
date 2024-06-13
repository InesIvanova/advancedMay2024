import re

with open("words.txt") as file:
    words = file.read()

words = words.split()

with open("input.txt") as file:
    text = file.read()


occ = {}

for word in words:
    # pattern = re.compile(f"\b{word}\b")
    pattern = rf"\b{word}\b"
    result = re.findall(pattern, text, re.IGNORECASE)
    occ[word] = len(result)

sorted_occ = sorted(occ.items(), key=lambda kvp: -kvp[1])

with open("output.txt", "w") as file:
    for key, value in sorted_occ:
        file.write(f"{key} - {value}\n")