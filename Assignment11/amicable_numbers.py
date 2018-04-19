# Taylor He, Jacob Manzelmann, Thomas Osterman
# Assignment 11: Project Euler #21 (Modified)
# I pledge my honor that I have abided by the Stevens Honor System.

import time
################## BRUTE FORCE ######################
def sum_factor(n):
    total = 0
    for i in range(1, n/2 + 1):
        if n % i == 0:
            total += i
    return total

def amicable_brute_force(size = 10000):
    amicables = []
    for i in range(1, size):
        s_fact = sum_factor(i)
        if (s_fact > i):
            if (sum_factor(s_fact) == i):
                amicables.append((i, s_fact))
    return amicables
#####################################################

################## O(n * sqrt(n))? ###############
def sum_factors_fast(n):
    """
    Same idea as sum_factors, but we only have to
    seach up to sqrt(n)
    """
    # Starts at 1 because 1 is a factor for every int
    total = 1
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            # If n%i==0, both n/i and i are in factors
            total += i + n/i 
    return total

def amicable_brute_opt(size = 100000):
    """
    Same idea as brute force, but checks less so it's optimized
    """
    # found is a set that checks for duplicates
    result = []
    found = set()
    for a in range(1, size+1):      # n
        b = sum_factors_fast(a)     # sqrt(n)
        if a < b and a == sum_factors_fast(b): # sqrt(n)
            amic_pair = (a, b)
            if amic_pair not in found:
                found.add(amic_pair)
                result += [amic_pair]
    return result

#####################################################


################## O(n^2) #####################
def amicable_fast(size = 1000000):
    """
    Instead of brute forcing, we can use a bit more
    memory to store factors and keep it in a divisors list
    Now that we generate the divisors, finding pairs takes 
    linear time with one pass
    Total time: O(n^2)
    """

    # Populate the divisors array with 2 for loops
    # The outer for loop is from 1-size
    #   The inner for loop is from 2 to a*b < size
    #       Set the divisor[index] += a
    #       where index is a*b, since a is a divisor of index
    amicables = []
    divisors = [0] * (size + 2)
    for a in range(1, size):
        for b in range(2, size/a + 1):
            divisors[a*b] += a
    
    # Now that we've built up a divisor list, it will look like a 
    # bunch of random numbers. However, a pair of amicable numbers 
    # will actually look like:  [..., 88730, ... , 79750] 
    #   where those numbers are at indexes 79750 and 88730, respectively
    
    # print divisors[79750], divisors[88730]

    # This part is confusing, since we have to access index of 
    # the value of the divisor for the actual number
    for i in range(1, len(divisors)):
        if (i < divisors[i] # the first number < second
            and divisors[i] <= size # keep both under size
            and divisors[divisors[i]] == i): # Check they are amicable
            amicables.append((i, divisors[i]))
    return amicables

###################################################

def speed_test(N):
    speed = {
        "BRUTE FORCE": (amicable_brute_force, [N/10]), # 100K takes too long (241741.51 ms)
        "FAST": (amicable_brute_opt, [N]),
        "FASTER": (amicable_fast, [N]),
    }
    print "Testing:\nBrute force at 10,000\nFast at 100,000\nFaster at 100,000"
    p = []
    for name in speed:
        start = time.time()
        [answer] = map(speed[name][0], speed[name][1])
        # total = sum([sum(tup) for tup in answer])
        # ans = "\n".join([str(tup) for tup in answer])
        end = time.time()
        # print ans
        # print 'Sum:', total
        p += [('{0} Time: {1:.2f} ms'.format(name, (end - start) * 1000))]
    print "\n".join(sorted(p)) + "\n"

def verification():
    """Psuedo-verification; checks if the num of pairs is correct
    Manually verified works till 22.3M, probs more too
    22,300,000 has 142 amicable pairs
    Really should be checking for Sum, but I'm too lazy to add them
    """
    start = time.time()
    answer = amicable_even_faster(223 * 100 * 1000)
    assert len(answer) == 142
    end = time.time()
    print 'Time: {0:.2f} ms'.format((end - start) * 1000)


if __name__ == '__main__':
    # Constants
    N = 100000
    RUN_SPEED_TESTS = False        # Speed tests
    RUN_VERIFICATION = False       # Verify fast version

    if RUN_SPEED_TESTS:
        speed_test(N)              # Compares speed between 3 versions
    if RUN_VERIFICATION:
        verification()             # Tests for 22.3M! AHHH!

    # The actual program
    start = time.time()

    answer = amicable_fast(N)
    total = sum([sum(tup) for tup in answer])
    ans = "\n".join([str(tup) for tup in answer])

    end = time.time()
    print ans
    print 'Sum:', total
    print 'Time: {0:.2f} ms'.format((end - start) * 1000)


