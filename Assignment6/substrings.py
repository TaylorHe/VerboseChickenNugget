# Taylor He, Jacob Manzelmann, Thomas Osterman
# CS370
# I pledge my honor that I have abided by the Stevens Honor System.
import sys

def sum_substr_of_int(balls):
    '''
        Given a number as a string, find the sum of all
        substrings that can be made by the number
        For example,
        '12' -> 15
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
            3, 34            => (3 + 30) * 3
            4                => (4) * 4

        ======================================================
        That means that for each n[i], we add the following sum
        i+1 times:
            (n[i] * 10^0) + (n[i] * 10^1) + ... + (n[i] * 10^(l-i))
        where l = len(n)

        This can be simplified to (i+1) * (n[i] * 111...11)
        This formula should be repeated for i in range(len(n))
        
        ======================================================

        =============== EDIT FOR HACKERRANK ==================
        link: www.hackerrank.com/challenges/sam-and-substrings/problem

        The hackerrank calls for a modulus, since balls can be
        very large (heehee) and therefore the sum can be very large

        We have to optimize for larger numbers. How?
        
        One modification made is to the "ones multiplier", which
        is the denoted by int('1' * (l-i)) as shown above

        Because 111..111 can be very large, it would make sense 
        to mod the multiplier before doing the mult calculation.

        We should be keeping track of this ones_multiplier instead 
        of calculating it straight up using int('1' * (l-i))
        
        ======================================================
    '''
    result = 0          # to return
    l = len(balls)      # len
    ones_multiplier = 0 # '1111...111'
    mod = 10**9 + 7     # modulus for hackerrank

    for i in range(l):
        # ones_multiplier = '1111...111' % mod
        ones_multiplier = (10 * ones_multiplier + 1) % mod
        # result is calculated by the equation:
        #    (n[i] * 10^0) + (n[i] * 10^1) + ... + (n[i] * 10^(l-i))
        # but with a modulus twist to keep numbers under mod
        result = (result + (int(balls[l-i-1]) * (l-i) * ones_multiplier) % mod) % mod
    
    return result 

if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise Exception("Usage: python sum.py <number>")
    print sum_substr_of_int(sys.argv[1])

    # For testing purposes:
    # with open(sys.argv[1]) as f:
    #     print sum_substr_of_int(f.read())


