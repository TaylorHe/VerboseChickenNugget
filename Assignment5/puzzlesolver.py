# puzzlesolver solves the Scramble Squares problem.
# Taylor He, Jacob Manzelmann, Thomas Osterman
# CS370
# I pledge my honor that I have abided by the Stevens Honor System.

import sys

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
    box = "+--------+--------+--------+\n".format(sol[0])
    
    line = ""
    # Generate first box row
    for i in range(3):
        line += "|{}  {}   ".format(sol[i], ftext[sol[i]][0])
    line += "|\n"

    # Second box row
    for i in range(3):
        line += "|{}    {}".format(ftext[sol[i]][3], ftext[sol[i]][1])
    line += "|\n"

    for i in range(3):
        line += "|   {}   ".format(ftext[sol[i]][2])

    box += line
def output(ftext, sol):
    '''
    Handles output
    '''
    # prints input in format
    for i in range(1,10):
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

    for solution in ssol:
        generate_solution_visual(solution, ftext)
    pass

def solve(parsed_data):
    '''
    Solves the scramble squares puzzle using brute force with pruning
    The solution should return a tuple:
        ("1234567890",  { 
                            1 : [4 edges in order (top right bot left)],
                            2:  [4 edges in order]
                        }
        )
    '''
    # TODO
    pass

def strip_same_solutions(sol):
    ''' 
    If a solution is found, 3 other solutions are equivalent. 
    Only take the numerically lowest solution.
    @param: list of solutions
    @return: list of solution stripped
    '''
    return [1,2]


if __name__=="__main__":
    '''Handle command line args'''
    if len(sys.argv) != 2:
        raise Exception("Usage: python puzzlesolver <filename>")
    with open(sys.argv[1], 'r') as f:
        # First parse the data into list of lists
        pdata = parse_input(f.read())
        # Solve
        soln = solve(pdata)
        # Print
        output(pdata, soln)

    
