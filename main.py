def return_correct_index(index):
    if index >= len(matrix[0]):
        return 0
    elif index < 0:
       return len(matrix[0]) - 1
    return index


direction_mapper = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1),
    "right_diagonal_up": (-1, 1),
    "left_diagonal_down": (1, -1),
    "left_diagonal_up": (-1, -1),
    "right_diagonal_down": (1, 1)

}
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]


current_row_index = 1
current_col_index = 2
row_movement, col_movement = direction_mapper['right']
desired_row_index = current_row_index + row_movement
desired_col_index_index = current_col_index + col_movement

row_index = return_correct_index(desired_row_index)
col_index = return_correct_index(desired_col_index_index)





