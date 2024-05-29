n = int(input())

matrix = []
for _ in range(n):
    row_data = list(input())
    matrix.append(row_data)

symbol = input()
position = None

for row_index in range(n):
    for col_index in range(n):
        if matrix[row_index][col_index] == symbol:
            position = (row_index, col_index)
            print(position)
            exit()

print(f"{symbol} does not occur in the matrix")
