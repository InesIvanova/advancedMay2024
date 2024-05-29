rows_count = int(input())

flattend = []

for i in range(rows_count):
    # row_data = [int(el) for el in input().split(", ")]
    flattend.extend([int(el) for el in input().split(", ")])


print(flattend)

