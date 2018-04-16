#!/bin/python
import os
import sys

def rabin_hash(s, d=5294212309, q=9743212277):
    """Implementation of the Rabin Fingerprint Hash
    TODO: NOT FINISHED
    """
    l = len(s)
    p = 0
    for c in s:
        p = (d*p+ord(c))%q
    return p

def rabin_karp_search_old(pattern, s):
    """Checks if pattern occurs in/is a substring of s
    This function is more promising than the horrid rabin_karp_search,
    but I don't know yet. It's not finished.
    """
    m, n = len(pattern), len(s)
    pattern_hash = rabin_hash(pattern)
    for i in range(1, n-m+1):
        # Check if the hash and values are the same
        if (rabin_hash(s[i:i+m-1]) == pattern_hash
            and s[i:i+m-1] == pattern):
            return True
    return False

def rabin_karp_search(pattern, s, d=257, q=11):
    """This is too slow. Fuck."""
    m, n = len(pattern), len(s)
    
    # h = pow(d,m-1)%q
    # pow() might take a while for large m, so mod as we go
    h = 1
    for _ in range(m-1):
        h = (d * h)%q
    p, t = 0, 0
    result = []
    for i in range(m): 
        p = (d*p+ord(pattern[i]))%q
        t = (d*t+ord(s[i]))%q
    for k in range(n-m+1):
        if p == t: # check character by character
            match = True
            for i in range(m):
                if pattern[i] != s[k+i]:
                    match = False
                    break
            if match:
                result = result + [k]
        if k < n-m:
            t = (t-h*ord(s[k]))%q 
            t = (t*d+ord(s[k+m]))%q 
            t = (t+q)%q 
    return result

def buildString(A, B, S):
    """Finds the lowest cost of making a string given
    append cost A, substring copy cost B, and target string S
    """
    # specify if you want to use the the rabin karp search
    RABIN_VERSION = False  

    cost = [0] + ([300000000] * len(S))
    copy_length = min(1, B/A)
    for i in range(1, len(cost)):
        cost[i] = min(cost[i], cost[i-1] + A)

        # while you are in range AND it makes sense to copy
        # AND you are able to copy, do it.
        j = copy_length
        if RABIN_VERSION:
            while j <= i and i < len(cost) - j and rabin_karp_search(S[i:i+j], S[:i]):
                cost[i+j] = min(cost[i+j], cost[i] + B)
                j += 1
        else: 
            while j <= i and i < len(cost) - j and S[i:i+j] in S[:i]:
                cost[i+j] = min(cost[i+j], cost[i] + B)
                j += 1

    return cost[-1]

if __name__ == '__main__':
    print buildString(4, 5, 'aabaacaba')
    print buildString(8, 9, 'bacbacacb')


# THIS IS FOR HACKERRANK
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     t = int(raw_input())

#     for t_itr in xrange(t):
#         nab = raw_input().split()

#         n = int(nab[0])

#         a = int(nab[1])

#         b = int(nab[2])

#         s = raw_input()

#         result = buildString(a, b, s)
#         fptr.write(str(result) + "\n")

#     fptr.close()
