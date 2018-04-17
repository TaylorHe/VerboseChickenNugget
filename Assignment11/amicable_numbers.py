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

################## O(n * sqrt(n)) ###############
def sum_factors_fast(n):
    """
    Same idea as sum_factors, but we only have to
    seach up to sqrt(n)
    """
    result = []
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            # If n%i==0, both n/i and i are in factors
            result += [i, n/i] 
    # Plus one because 1 is a factor for every int
    return sum(result)+1

def amicable_fast(size = 100000):
    """
    Same idea as brute force, but checks less
    """
    # found is a set that checks for duplicates
    result = []
    found = set()
    for a in range(1, size+1):
        b = sum_factors_fast(a)
        if a != b and a == sum_factors_fast(b):
            amic_pair = (min(a,b), max(a,b))
            if amic_pair not in found:
                found.add(amic_pair)
                result += [amic_pair]
    return result

#####################################################


################## O(n^2) #####################
def amicable_even_faster_doesnt_work(size = 100000):
    """
    =======BROKEN=======
    Instead of brute forcing, we can use a bit more
    memory to store factors and keep it in a divisors list
    Now that we generate the divisors, finding pairs takes 
    linear time with one pass
    Total time: O(n^2)
    """

    # Populate the divisors array with 2 for loops
    # The outer for loop is from 1-n
    #   The inner for loop is from 2 to a*b < n
    #       Set the divisor[index] += a
    #       where index is a*b, since that's what it's multiplying up to
    amicables = []
    divisors = [0] * (size*size) # this part is bounded by some number, dunno what
    for a in range(1, size+1):
        for b in range(2, size):
            divisors[a*b] += a
    # print m
    # print max(divisors)
    # print divisors

    # This part is really confusing, since we have to access index of 
    # the value of the divisor for the actual number
    for i in range(1, len(divisors)):
        if i < divisors[i] and divisors[divisors[i]] == i:
            amicables.append((i, divisors[i]))
    return amicables

###################################################

if __name__ == '__main__':
    # Constants
    N = 100000
    speed = {
        "BRUTE FORCE": (amicable_brute_force, [N]), 
        "FAST": (amicable_fast, [N]) 
        # "FASTER": (amicable_even_faster, [N*10])
    }
    print "Testing:\nBrute force at 100,000 \nFast at 100,000\n"
    p = []
    for name in speed:
        start = time.time()
        [answer] = map(speed[name][0], speed[name][1])
        total = 0;

        for tup in answer:
            # print tup
            total += sum(tup)
        end = time.time()
        # print'Sum:', total
        p += [('{0} Time: {1:.2f} ms'.format(name, (end - start) * 1000))]
    print "\n".join(sorted(p)) + "\n"
    ### FASTEST

    print "Now testing fast at 100,000"
    start = time.time()
    answer = amicable_fast(100000)
    total = 0;

    for tup in answer:
        print tup
        total += sum(tup)
    end = time.time()
    print 'Sum:', total
    print 'Time: {0:.2f} ms'.format((end - start) * 1000)


