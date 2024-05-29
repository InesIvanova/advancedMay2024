data = input().split(", ")
row_number, col_number = int(data[0]), int(data[1])

# matrix = []
# sum_nums = 0
#
# for row in range(row_number):
#     data_row = input().split(", ")
#     row_numbers = []
#     for index in range(len(data_row)):
#         current_element = int(data_row[index])
#         sum_nums += current_element
#         row_numbers.append(current_element)
#     matrix.append(row_numbers)
# print(sum_nums)
# print(matrix)

matrix = []
sum_nums = 0

for i in range(row_number):
    rows_nums = [int(el) for el in input().split(", ")]
    sum_nums += sum(rows_nums)
    matrix.append(rows_nums)


for row in matrix:
    print(row)


