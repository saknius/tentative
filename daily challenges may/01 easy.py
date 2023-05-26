
def max_diagonal_sum(matrix):
    row_len = len(matrix)
    col_len = len(matrix[0])
    first_diagonal = 0
    second_diagonal = 0
    for row_itr in range(row_len):
        for col_itr in range(col_len):
            if row_itr == col_itr:
                first_diagonal += matrix[row_itr][col_itr]
            if row_len - 1 - row_itr == col_itr:
                second_diagonal +=  matrix[row_itr][col_itr]
    print(first_diagonal, second_diagonal)
    return max(first_diagonal, second_diagonal)

if __name__ == '__main__':
    matrix =  [[2,1,1,3],
              [1,1,1000,1],
              [1,1,1,1],
              [1,1,1,1]]
    print(max_diagonal_sum(matrix))


# time taken : undefined
# expected time complexity : O(n*m)
# acheivable time complexity : O(1) maybe idk
# required time complexity : O(n*m)
# expected space complexity : O(n*m)
# acheivable space complexity : O(1) maybe idk
# required space complexity : O(n*m)
# relative tuffness : super easy
