# puzzlesolver solves the Scramble Squares problem.
# Taylor He, Jacob Manzelmann, Thomas Osterman
# CS370
# I pledge my honor that I have abided by the Stevens Honor System.

import sys

num_soutions = 0
solutions = []
# for the board yellow=1 green=2, red=3, blue=4
# positive is head, negative is tail
board = [ [0]*4 for _ in range(9) ]
# board = [[0,0,0,0], [0,0,0,0], [0,0,0,0], 
#          [0,0,0,0], [0,0,0,0], [0,0,0,0], 
#          [0,0,0,0], [0,0,0,0], [0,0,0,0]]

def parse_input(file):
    '''
    Parses the text file. Returns a dictionary with num:lists in the form
    [
(INDEX0)    1 : [EDGE, EDGE, EDGE, EDGE],
(INDEX1)    2 : [EDGE, EDGE, EDGE, EDGE],
            3 : [EDGE, EDGE, EDGE, EDGE],
            4 : [EDGE, EDGE, EDGE, EDGE],
            5 : [EDGE, EDGE, EDGE, EDGE],
            6 : [EDGE, EDGE, EDGE, EDGE],
            7 : [EDGE, EDGE, EDGE, EDGE],
            8 : [EDGE, EDGE, EDGE, EDGE],
            9 : [EDGE, EDGE, EDGE, EDGE]
    ]
    '''
    ret = []
    for index, tile in enumerate(file.split('\n')):
        ret.append([edge for edge in tile.split(',')])
    return ret

def generate_solution_visual(sol, ftext):
    '''
    sol is given as tuple: (a string "1234567890", [EDGE * 4] in order)
    ftext is given as {number : [EDGE] * 4}
    '''

    order = sol[0]
    edge_order = sol[1]

    horiz = "+--------+--------+--------+"
    box = horiz + "\n"
    
    line = ""
    # Generate first box row
    for i in range(3):
        line += "|{}  {}   ".format(order[i], edge_order[int(order[i])][0])
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

    print box
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
    print "{} unique solution".format(len(ssol)) + ("s" if len(ssol) != 1 else "") + " found:"
    
    # Print all solutions

    #for solution in ssol:
    generate_solution_visual(ssol, ftext)
    pass

def solve(parsed_data, num):
    '''
    Solves the scramble squares puzzle using brute force with pruning
    The solution should return a tuple:
        ("1234567890",  { 
                            1 : [4 edges in order (top right bot left)],
                            2 : [4 edges in order]
                        }
        )
    '''
    # TODO
    for i in range(1,10):
        #add piece
        for j in range(4):
            if valid(i-1):
                solve(num+1)
            rotate(parsed_data[num])
    pass

def rotate(piece):
    temp = piece[0]

def enumerate_data(data):
    numdata = {}
    for i in range(1,10):
        temp = []
        for j in range(4):
            if data[i][j] == "Y0":
                temp.append(-1)
            elif data[i][j] == "Y1":
                temp.append(1)
            elif data[i][j] == "G0":
                temp.append(-2)
            elif data[i][j] == "G1":
                temp.append(2)
            elif data[i][j] == "R0":
                temp.append(-3)
            elif data[i][j] == "R1":
                temp.append(3)
            elif data[i][j] == "B0":
                temp.append(-4)
            else:
                temp.append(4)
        numdata[i] = temp
    return numdata

def strip_same_solutions(sol):
    ''' 
    If a solution is found, 3 other solutions are equivalent. 
    Only take the numerically lowest solution.
    @param: list of solutions
    @return: list of solution stripped
    '''
    return ("123",  {
                        1 : ["A0", "B1", "C1", "D1"],
                        2 : ["A1", "B1", "C1", "D1"],
                        3 : ["A1", "B1", "C1", "D1"]
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

    
