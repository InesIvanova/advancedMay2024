from sys import maxsize

row_count, col_count = [int(el) for el in input().split(", ")]

matrix = []

for _ in range(row_count):
    row_data = [int(el) for el in input().split(", ")]
    matrix.append(row_data)



max_sum = -maxsize

sub_matrix = None
for row_index in range(row_count-1):
    for col_index in range(col_count-1 ):
        current_element = matrix[row_index][col_index]
        next_element = matrix[row_index][col_index + 1]
        element_below = matrix[row_index+1][col_index]
        element_diagonal = matrix[row_index + 1][col_index+1]
        current_sum = sum((current_element, next_element, element_below, element_diagonal))

        if current_sum > max_sum:
            max_sum = current_sum
            sub_matrix = [[current_element, next_element], [element_below, element_diagonal]]


if sub_matrix:
    print(*sub_matrix[0], sep=" ")
    print(*sub_matrix[1], sep=" ")

print(max_sum)
