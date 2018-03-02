# puzzlesolver solves the Scramble Squares problem.
# Taylor He, Jacob Manzelmann, Thomas Osterman
# CS370
# I pledge my honor that I have abided by the Stevens Honor System.

import sys

num_solutions = 0
# for the board yellow=1 green=2, red=3, blue=4
# positive is head, negative is tail
board = [ [0]*4 for _ in range(9) ]
# board = [[0,0,0,0], [0,0,0,0], [0,0,0,0],
#          [0,0,0,0], [0,0,0,0], [0,0,0,0],
#          [0,0,0,0], [0,0,0,0], [0,0,0,0]]
color_map = {"Y0" : -1, "Y1" : 1, "G0" : -2, "G1" : 2,
             "R0" : -3, "R1" : 3, "B0" : -4, "B1" : 4}

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

def generate_solution_visual(sol, ftext):
    '''
    sol is given as tuple: (a string "1234567890", [EDGE * 4] in order)
    ftext is given as {number : [EDGE] * 4}
    '''

    order = sol[0]
    edge_order = sol[1]
    for k in range(3):
        line = ""
        horiz = "+--------+--------+--------+"
        box = horiz + "\n"

        # Generate first box row
        for i in range(3):
            line += "|{}  {}   ".format(order[i+3*k], edge_order[int(order[i])][0])
        line += "|\n"

        # Second box row
        for i in range(3):
            tile = edge_order[int(order[i])]
            line += "|{}    {}".format(tile[3], edge_order[int(order[i])][1])
        line += "|\n"

        for i in range(3):
            line += "|   {}   ".format(edge_order[int(order[i])][2])
        line += "|\n"

        box += line + horiz
        if rowno != 2: box += '\n'

    return box

def output(ftext, sol):
    '''
    Handles output
    '''
    # prints input in format
    for i in range(9):
        tile = ftext[i]
        print "{}. <{}, {}, {}, {}>".format(i, tile[0], tile[1], tile[2], tile[3]);

    # Here we print the solution.
    # First strip duplicate solutions
    ssol = strip_same_solutions(sol)

    if ssol == []:
        print "\nNo solution found."
        return
    print "\n{} unique solution".format(len(ssol)) + ("s" if len(ssol) != 1 else "") + " found:"

    # Print all solutions

    #for solution in ssol:
    generate_solution_visual(ssol, ftext)
    pass

used = [False]*10

def solve(parsed_data):
    return solve_helper(parsed_data, 0 , "", [])

def solve_helper(data, num, order, solutions):
    '''
    Solves the scramble squares puzzle using brute force with pruning
    The solution should return a tuple:
        ("1234567890",  {
                            1 : [4 edges in order (top right bot left)],
                            2 : [4 edges in order]
                        }
        )
    '''
    if num == 9:
        num_solutions += 1
        solutions.append((order, data))
        return (order, solutions)
    for i in range(1,10):
        if not used[i]:
            used[i] = True
            for j in range(4):
                board[i-1] = data[i]
                order += str(i-1)
                if valid(i-1):
                    solve_helper(num+1)
                rotate(data[i])
            used[i] = False
            board[i-1] = [0,0,0,0]
            order = order[:-1]

    return (order, solutions)

def valid(num):
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
    order = set([tup[0] for tup in sol])
    remove_set = set()
    for item in order:
        rotate_num = ""
        for i in range(6,-1,-3): rotate_num += item[i]
        for i in range(7,0,-3): rotate_num += item[i]
        for i in range(8,0,-3): rotate_num += item[i]
        if rotate_num in order:
            if int(item) < int(rotate_num):
                remove_set.add(rotate_num)
            else:
                remove_set.add(item)
    for i in remove_set: order.remove(i)
    print order


    #[ ("123456789", orientation), ("123456789", orientation) ]
    return ("124967385",  {
                        1 : ["A0", "B1", "C1", "D1"],
                        2 : ["A1", "B1", "C1", "D1"],
                        3 : ["A1", "B1", "C1", "D1"],

                        4 : ["A0", "B1", "C1", "D1"],
                        5 : ["A1", "B1", "C1", "D1"],
                        6 : ["A1", "B1", "C1", "D1"],

                        7 : ["A0", "B1", "C1", "D1"],
                        8 : ["A1", "B1", "C1", "D1"],
                        9 : ["A1", "B1", "C1", "D1"]
                    })


if __name__=="__main__":
    '''Handle command line args'''
    if len(sys.argv) != 2:
        raise Exception("Usage: python puzzlesolver <filename>")
    with open(sys.argv[1], 'r') as f:
        # First parse the data into list of lists
        pdata = parse_input(f.read())
        # Change data into numbers
        numdata = enumerate_data(pdata)
        # Solve
        soln = solve(numdata)
        # Print
        output(pdata, soln)
