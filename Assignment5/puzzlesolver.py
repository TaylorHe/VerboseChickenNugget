# puzzlesolver solves the Scramble Squares problem.
# Taylor He, Jacob Manzelmann, Thomas Osterman
# CS370
# I pledge my honor that I have abided by the Stevens Honor System.

import sys

def parse_input(file):
    '''
    Parses the text file. Returns a list of lists in the form
    [
        [EDGE, EDGE, EDGE, EDGE],
        [EDGE, EDGE, EDGE, EDGE],
        [EDGE, EDGE, EDGE, EDGE],
        [EDGE, EDGE, EDGE, EDGE],
        [EDGE, EDGE, EDGE, EDGE],
        [EDGE, EDGE, EDGE, EDGE],
        [EDGE, EDGE, EDGE, EDGE],
        [EDGE, EDGE, EDGE, EDGE],
        [EDGE, EDGE, EDGE, EDGE]
    ]
    '''
    ret = []
    for tile in file.split('\n'):
        ret.append([edge for edge in tile.split(',')])
    return ret


def output(ftext, sol):
    '''
    Handles output
    '''
    for index, tiles in enumerate(ftext):
        print "{}. <{}, {}, {}, {}>".format(index+1, tiles[0], tiles[1], tiles[2], tiles[3]);
    # Here we print the solution.
    # TODO
    pass

def solve(parsed_data):
    '''
    Solves the scramble squares puzzle using brute force with pruning
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

    
