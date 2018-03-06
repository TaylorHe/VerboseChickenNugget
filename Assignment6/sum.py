# Taylor He, Jacob Manzelmann, Thomas Osterman
# CS370
# I pledge my honor that I have abided by the Stevens Honor System.
import sys

def sum_substr_of_int(n):
    '''
        Given a number as a string, find the sum of all
        substrings that can be made by the number
        For example,
        '12'  -> 15
            1 + 2 + 12 = 15
        '8734' -> 10557
            8 + 7 + 3 + 4 +
            87 + 73 + 34 +
            873 + 734 + 
            8734 = 10557

        If we take a closer look at the string, we can reorganize
        the substrings as follows:
        '8734' ->
            8, 87, 873, 8734 => 8 + 80 + 800 + 8000 
            7, 73, 734       => (7 + 70 + 700) * 2      (from above)
            3, 34            => (3 + 34) * 3
            4                => (4) * 4

        ======================================================
        That means that for each n[i], we add the following sum
        i+1 times:
            (n[i] * 10^0) + (n[i] * 10^1) + ... + (n[i] * 10^(l-i))
        where l = len(n)

        **This can be simplified to (i+1) * (n[i] * 111...11)**
        This formula should be repeated for i in range(len(n))
        
        ======================================================
    '''
    result = 0
    l = len(n)
    for i in range(l):
        # (n[i] * 10^0) + (n[i] * 10^1) + ... + (n[i] * 10^(l-i))
        result += ((i+1) * int(n[i]) * int('1' * (l-i)))
    return result

if __name__ == '__main__':
    # print sys.argv[1]
    if len(sys.argv) != 2:
        raise Exception("Usage: python sum.py <number>")
    print sum_substr_of_int(sys.argv[1])

'''
Testing: 
    '12' -> 15
        1 + 2 + 12
    '123' -> 164
        1 + 2 + 3 + 12 + 23 + 123
    '8734' -> 10557
        8 + 7 + 3 + 4 +
        87 + 73 + 34 +
        873 + 734 + 
        8734
'''