def check_list_have_num(matrix, target):
    row = len(matrix)
    col = len(matrix[0])

    i = row-1
    j = 0

    while j < col and i >= 0:
        if target < matrix[i][j]:
            i -= 1
        elif target > matrix[i][j]:
            j += 1
        else:
            return True
    return False


matrix = [
    [1,   4,  7, 11, 15],
    [2,   5,  8, 12, 19],
    [3,   6,  9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]
target = 5

print(check_list_have_num(matrix, target))
