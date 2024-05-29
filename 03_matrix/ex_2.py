row_num = int(input())
matrix = []

for i in range(row_num):
    row_data = [int(el) for el in input().split(", ") if int(el) % 2 == 0]
    matrix.append(row_data)
print(matrix)