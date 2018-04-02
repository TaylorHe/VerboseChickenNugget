'''
CS370 Assignment 8
Solves ProjectEuler #82
Taylor He, Jacob Manzelmann, Tommy Osterman
I pledge my honor that I have abided by the Stevens Honor System
'''
import sys

def backtrack(matrix, dp_matrix, row, col):
    path = []
    while True:
        diff = dp_matrix[row][col] - matrix[row][col]
        path.append(matrix[row][col])

        # If we can traverse left, do it
        if diff == dp_matrix[row][col-1]:
            col -= 1
        # If col == 0 (We are at the left col), 
        # then break because we are done
        elif col == 0:
            break
        # If we can go down, do that
        elif row + 1 < len(matrix) and diff == dp_matrix[row+1][col]:
            row += 1
        # Else we should traverse up
        elif row >= 1 and diff == dp_matrix[row-1][col]:
            row -= 1
        
    return list(reversed(path))


def solve(matrix):
    '''Solves ProjectEuler 82 using DP'''
    size = len(matrix)
    # If size == 1, trivial case
    if size == 1:
        print('Min sum:', matrix[0][0])
        print('Values:', [matrix[0][0]])
        return

    # Allocate dp matrix
    dp_matrix = []
    for _ in range(size):
        dp_matrix.append([None for _ in range(size)])

    # Populate the left column with the only option
    for row in range(size):
        dp_matrix[row][0] = matrix[row][0]

    # print("dp", dp_matrix)
    # print(matrix)

    for col in range(1, size):
        # The upper row can only come from the left
        dp_matrix[0][col] = dp_matrix[0][col - 1] + matrix[0][col]

        # Traverse the row moving downward
        for row in range(1, size):
            dp_matrix[row][col] = matrix[row][col] + min(dp_matrix[row-1][col], dp_matrix[row][col-1])

        # Then traverse back up the row, changing values when necessary
        for row in range(size-2, -1, -1):
            dp_matrix[row][col] = min(dp_matrix[row][col], matrix[row][col] + dp_matrix[row+1][col])

    # print("dp", dp_matrix)
    
    minSum = dp_matrix[0][size-1]
    start = 0
    for row in range(1, size):
        if dp_matrix[row][size-1] < minSum:
            minSum = dp_matrix[row][size-1]
            start = row

    print('Min sum:', minSum)
    print('Values:', backtrack(matrix, dp_matrix, start, size-1))


if __name__ == '__main__':
    # If given a parameter, use that as filename instead.
    filename =  'matrix.txt' if len(sys.argv) == 1 else sys.argv[1]
    matrix = []
    with open(filename, 'r') as f:
        for line in f:
            matrix.append([int(x) for x in line.split(',')])
    solve(matrix)
