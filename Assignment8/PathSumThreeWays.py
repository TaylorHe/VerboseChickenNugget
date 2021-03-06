'''
CS370 Assignment 8
Solves ProjectEuler #82
Taylor He, Jacob Manzelmann, Tommy Osterman
I pledge my honor that I have abided by the Stevens Honor System
'''
import sys

def backtrack(matrix, dp_matrix, row):
    '''Backtracks the matrix, starting at the given row'''
    col = len(matrix) - 1
    path = []
    while col != 0:
        diff = dp_matrix[row][col] - matrix[row][col]
        path.append(matrix[row][col])
        # If we can traverse left, do it
        if diff == dp_matrix[row][col-1]:
            col -= 1
        # If col == 0 (We are at the left col), then break because we are done
        # If we should go down, do that
        elif row + 1 < len(matrix) and diff == dp_matrix[row+1][col]:
            row += 1
        # Else we should traverse up
        elif row >= 1 and diff == dp_matrix[row-1][col]:
            row -= 1

    # When col == 0, append the last item and break
    path.append(matrix[row][0])
    return path[::-1]


def solve(matrix):
    '''Solves ProjectEuler 82 using DP
    returns (solution, path)
    '''
    size = len(matrix)
    # If size == 1, trivial case
    if size == 1:
        return (matrix[0][0], matrix[0])

    # Allocate dp matrix
    dp_matrix = [[None] * size for _ in range(size)]

    # Populate the left column with the only option
    for row in range(size):
        dp_matrix[row][0] = matrix[row][0]

    # Start building the dp matrix
    for col in range(1, size):
        # The upper row can only come from the left
        dp_matrix[0][col] = dp_matrix[0][col - 1] + matrix[0][col]

        # Traverse the row moving downward
        for row in range(1, size):
            dp_matrix[row][col] = matrix[row][col] + min(dp_matrix[row-1][col], dp_matrix[row][col-1])

        # Then traverse back up the row, changing values when necessary
        for row in range(size-2, -1, -1):
            dp_matrix[row][col] = min(dp_matrix[row][col], matrix[row][col] + dp_matrix[row+1][col])

    # After we are done building the table, find the min sum and its index
    min_sum = dp_matrix[0][size-1]
    start = 0
    for row in range(1, size):
        if dp_matrix[row][size-1] < min_sum:
            min_sum = dp_matrix[row][size-1]
            start = row

    return (min_sum, backtrack(matrix, dp_matrix, start))
    

def print_sol(min_sum, path):
    '''Prints the solution as specified in the homework'''
    print('Min sum:', min_sum)
    print('Values:', path)



if __name__ == '__main__':
    # If given a parameter, use that as filename instead.
    filename =  'matrix.txt' if len(sys.argv) == 1 else sys.argv[1]
    matrix = []
    with open(filename, 'r') as f:
        for line in f:
            matrix.append([int(x) for x in line.split(',')])

    # Solve and print
    (min_sum, path) = solve(matrix)

    print_sol(min_sum, path)
