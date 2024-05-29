numbers = tuple([float(num) for num in input().split()])

occurrences = {}

for num in numbers:
    if num not in occurrences:
        occurrences[num] = numbers.count(num)

for key, value in occurrences.items():
    print(f"{key:.1f} - {value} times")