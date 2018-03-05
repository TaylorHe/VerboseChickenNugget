# puzzlesolver solves the Scramble Squares problem.
# Taylor He, Jacob Manzelmann, Thomas Osterman
# CS370
# I pledge my honor that I have abided by the Stevens Honor System.
#import time
import sys

# for the board yellow=1 green=2, red=3, blue=4
# positive is head, negative is tail
color_map = {
    "Y0" : -1, "Y1" : 1, 
    "G0" : -2, "G1" : 2,
    "R0" : -3, "R1" : 3, 
    "B0" : -4, "B1" : 4
}
reverse_color_map = {
    -1 : "Y0", 1 : "Y1",
    -2 : "G0", 2 : "G1",
    -3 : "R0", 3 : "R1",
    -4 : "B0", 4 : "B1"
}

def parse_input(file):
    '''
    Parses the text file. Returns a dictionary with num:lists in the form
    {
            1 : [EDGE, EDGE, EDGE, EDGE],
            2 : [EDGE, EDGE, EDGE, EDGE],
            3 : [EDGE, EDGE, EDGE, EDGE],
            4 : [EDGE, EDGE, EDGE, EDGE],
            5 : [EDGE, EDGE, EDGE, EDGE],
            6 : [EDGE, EDGE, EDGE, EDGE],
            7 : [EDGE, EDGE, EDGE, EDGE],
            8 : [EDGE, EDGE, EDGE, EDGE],
            9 : [EDGE, EDGE, EDGE, EDGE]
    }
    '''
    ret = {}
    for index, tile in enumerate(file.split('\n')):
        ret[index+1] = [edge for edge in tile.split(',')]
    return ret

def generate_solution_visual(order, edge_order):
    '''
    Produces the visual representations of all solutions
    '''

    horiz = "+--------+--------+--------+"
    box = horiz + "\n"
    for k in range(3):
        line = ""

        # Generate first box row
        # print "order", order
        # print "edge", edge_order
        for i in range(3):
            line += "|{}  {}   ".format(order[i+3*k], reverse_color_map[edge_order[int(order[i+3*k])][0]])
        line += "|\n"

        # Second box row
        for i in range(3):
            tile = edge_order[int(order[i+3*k])]
            line += "|{}    {}".format(reverse_color_map[tile[3]], reverse_color_map[tile[1]])
        line += "|\n"

        for i in range(3):
            line += "|   {}   ".format(reverse_color_map[edge_order[int(order[i+3*k])][2]])
        line += "|\n"

        box += line + horiz
        if k != 2: box += '\n'

    return box + "\n"

def output(ftext, sol):
    '''
    Handles output
    
    sol is given as tuple: (a string "1234567890", [EDGE * 4] in order)
    ftext is given as {number : [EDGE] * 4}
    '''
    # prints input in format
    print "Input tiles:"
    for i in range(1,10):
        tile = ftext[i]
        print "{}. <{}, {}, {}, {}>".format(i, tile[0], tile[1], tile[2], tile[3]);

    # Here we print the solution.
    # First strip duplicate solutions
    ssol = strip_same_solutions(sol)

    if ssol == []:
        print "\nNo solution found."
        return
    print "\n{} unique solution".format(len(ssol)) + ("s" if len(ssol) != 1 else "") + " found:"

    for (order, edge_order) in ssol:
        print generate_solution_visual(order, edge_order)
    pass

def solve(parsed_data):
    # solutions array
    arr = []
    board = [ [0]*4 for _ in range(9) ]
    # board = [[0,0,0,0], [0,0,0,0], [0,0,0,0],
    #          [0,0,0,0], [0,0,0,0], [0,0,0,0],
    #          [0,0,0,0], [0,0,0,0], [0,0,0,0]]

    # Tells if a piece is used or not
    # Is length 10 for quicker acess with 1-9 dictionary indexes
    used = [False]*10
    solve_helper(parsed_data, 0 , "", arr, board, used)
    return arr

def solve_helper(data, num, order, solutions, board, used_pieces):
    '''
    Solves the scramble squares puzzle using brute force with pruning
    The solution should save a list of tuples in the form:
        ("1234567890",  {
                            1 : [4 edges in order (top right bot left)],
                            2 : [4 edges in order]
                        }
        )

    data: A list of lists containing color data for each piece
    num: The number of pieces placed so far
    order: The order in which the pieces have been placed
    solutions: A list of soultion tuples containing the order and rotation states of the pieces
    board: A board containing all pieces added so far
    used_pieces: A list of bools to determine which pieces have been used so far
    '''
    if num == 9:
        # make a copy so it is not a reference
        orientation = {}
        for index, d_item in enumerate(data):
            orientation[index+1] = [item for item in data[d_item]]

        # add solution
        solutions.append((order, orientation))
        return
    for i in range(1,10):
        # if the piece has been placed, don't use it
        if not used_pieces[i]:
            used_pieces[i] = True
            # check all piece orientations
            for j in range(4):
                board[num] = data[i]
                # recursively explore all valid statess
                if valid(num, board):
                    order += str(i)
                    solve_helper(data, num+1, order, solutions, board, used_pieces)
                    order = order[:-1]
                board[num] = [0,0,0,0]
                rotate(data[i])
            used_pieces[i] = False
    return

def valid(num, board):
    '''
    Checks if adding a tile to the current board is valid
    '''
    if num == 0:
        return True
        #the first and only piece is always valid
    if num < 3:
        return board[num][3] == board[num-1][1] * -1
        #the top row of tiles don't need to check above it
    elif num % 3 == 0:
        return board[num][0] == board[num-3][2] * -1
        #the first collumn of tiles don't need to check to the left of it
    return board[num][0] == board[num-3][2] * -1 and board[num][3] == board[num-1][1] * -1
    #otherwise check if the tile to the left and above it match


# Rotates a given piece
def rotate(piece):
    temp = piece.pop()
    piece.insert(0, temp)


# Turns the data into numbers for easier equivalence checking
def enumerate_data(data):
    numdata = {}
    for i in range(1,10):
        temp = []
        for j in range(4):
            temp.append(color_map[data[i][j]])
        numdata[i] = temp
    return numdata

def strip_same_solutions(sol):
    '''
    If a solution is found, 3 other solutions are equivalent.
    Only take the numerically lowest solution.
    @param: list of solutions
    @return: list of solution stripped
    '''
    order = {}
    for tup in sol: order[tup[0]] = tup[1]
    remove_set = set()
    for item in order.keys():
        curr = item
        for _ in range(3):
            rotate_num = ""
            for i in range(6,-1,-3): rotate_num += curr[i]
            for i in range(7,0,-3): rotate_num += curr[i]
            for i in range(8,0,-3): rotate_num += curr[i]
            if rotate_num in order:
                if int(item) < int(rotate_num):
                    remove_set.add(rotate_num)
                else:
                    remove_set.add(item)
            curr = rotate_num
    for i in remove_set: del order[i]
    
    o = sorted([i for i in order.keys()])
    return [(i, order[i]) for i in o]

    #[ ("123456789", orientation), ("123456789", orientation) ]
    # return ("124967385",  {
    #                     1 : ["A0", "B1", "C1", "D1"],
    #                     2 : ["A1", "B1", "C1", "D1"],
    #                     3 : ["A1", "B1", "C1", "D1"],

    #                     4 : ["A0", "B1", "C1", "D1"],
    #                     5 : ["A1", "B1", "C1", "D1"],
    #                     6 : ["A1", "B1", "C1", "D1"],

    #                     7 : ["A0", "B1", "C1", "D1"],
    #                     8 : ["A1", "B1", "C1", "D1"],
    #                     9 : ["A1", "B1", "C1", "D1"]
    #                 })


if __name__=="__main__":
    '''Handle command line args'''
    if len(sys.argv) != 2:
        raise Exception("Usage: python puzzlesolver <filename>")
    with open(sys.argv[1], 'r') as f:
        # First parse the data into dictionary of lists
        pdata = parse_input(f.read())
        
        # Change data into numbers
        numdata = enumerate_data(pdata)

        # Solve
        soln = solve(numdata)

        # Print
        output(pdata, soln)
