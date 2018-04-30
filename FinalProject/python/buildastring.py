# Taylor He, Jacob Manzelmann, Thomas Osterman
# I pledge my honor that I have abided by the Stevens Honor System.
# 
# Included in the file are the semi-working attempts at solving the problem
# specified by: 
#   https://www.hackerrank.com/challenges/build-a-string/problem
# In no specific order, the attempts we tried were:
#     - DP
#     - DP with memoization
#     - Greedy
#     - Rabin Karp with rolling hash
#     - Suffix Array pattern search

#!/bin/python
import os
import sys
import time


def build_string_rabin_karp(a, b, s):
    # d and p are random primes
    def rabin_karp_search(pattern, s, d=5294212309, q=9743212277):
        """ Rolling Hash:
        The idea is to not recompute and store the hash every time,
        as we can compute quickly the hash given the previous string
        
        """
        m, n = len(pattern), len(s)
        # h = pow(d,m-1)%q
        # mod as we go
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
    cost = [0] + ([2**31 - 1] * len(s))
    min_copy_length = min(1, b/a)   # At what length does it make sense to copy?
    for i in range(1, len(cost)):
        cost[i] = min(cost[i], cost[i-1] + a)
        # j <= i:            You can't copy more than you have already built
        # i + j < len(cost): You can't copy more than length of string
        # s[i:i+j] in s[:i]: The future string appears in the current one 
        j = min_copy_length
        while (j <= i and i + j < len(cost) and rabin_karp_search(s[i:i+j], s[:i])):
            cost[i+j] = min(cost[i+j], cost[i] + b)
            j += 1
    return cost[-1]

def suff_and_rank(s):
    suffix_array = [i for i in range(len(s)+1)]
    rank = [ord(s[i]) for i in range(len(s))] + [-1]
    # print rank, suffix_array, s
    k = 1
    
    # O(nlg(n))
    while k <= len(s):
        # Sort suffix array by rank
        def suffcmp(a, b):
            if rank[a] != rank[b]:
                return 1 if rank[a] < rank[b] else -1
            ra = rank[a+k] if a + k <= len(s) else -1
            rb = rank[b+k] if b + k <= len(s) else -1
            if ra != rb:
                return 1 if ra < rb else -1
            return 0
            # return 1 if (rank[a], ra) < (rank[b], rb) else -1

        suffix_array.sort(cmp=suffcmp, reverse=True)
        # do the DP
        dp = [0] * (len(s) + 1)
        dp[suffix_array[0]] = 0
        for i in range(len(s)):
            # The next item in the cost array is the previous suffix array index
            # plus 1 if prev rank < i+1 rank, or -1 if prev rank >= i+1 rank
            dp[suffix_array[i+1]] = dp[suffix_array[i]] + suffcmp(suffix_array[i], suffix_array[i+1])
        rank = dp
        k *= 2
    # print suffix_array, rank
    return suffix_array, rank

def find_longest_prefix(s, suffix_array, rank, start):
    """
    Finds the longest prefix length given the string, a precomputed 
    suffix array and its rank, and offset.
    """
    def where_differs(f, s):
        """Returns the index at which 2 strings differ"""
        i = 0
        while i < len(f) and f[i] == s[i]:
            i += 1
        return i

    ret = 0
    # Work down from rank
    i = rank[start]
    # print "i is:", i
    for i in range(rank[start], 0, -1):
        if (s[suffix_array[i]] != s[start]):
            break
        if suffix_array[i] <= start:
            continue
        # print "t:", s, "; offset:", start, print "; t+offset:", s[start]
        # Find the point at which the 2 arrays differ
        first = s[suffix_array[i]:]
        second = s[start:]
        dif = where_differs(s[suffix_array[i]:], s[start:])
        # print "L is:", dif
        if dif <= ret: break
        ret = max(ret, min(suffix_array[i] - start, dif))
    # print "start:", start, print "; s:", s
    for i in range(rank[start], len(suffix_array), 1):
        # print suffix_array[i]
        if s[suffix_array[i]-1] != s[start]: break
        if suffix_array[i] <= start: continue
        first = s[suffix_array[i]:]
        second = s[start:]
        dif = where_differs(s[suffix_array[i]:], s[start:])
        # print "l is:", distance_from_second
        if dif <= ret: break
        ret = max(ret, min(suffix_array[i] - start, dif))
    # print "ans:", ret
    return ret


def build_string_suffix(a, b, s):
    s2 = s[::-1]
    suffix_array, rank = suff_and_rank(s2)
    cost = [0] * (len(s) + 1)
    for i in range(len(s)):
        # Populate dp cost array
        cost[i+1] = cost[i] + a
        longest_prefix = find_longest_prefix(s2, suffix_array, rank, len(s)-i-1)
        for j in range(longest_prefix):
            cost[i+1] = min(cost[i+1], cost[i-j] + b)
    return cost[-1]

def build_string_dp_memo(a, b, s):
    """ Finds the lowest cost to build a string using DP
    and a found substring cache
    """
    cost = [0] + ([2**31 - 1] * len(s))
    found_substrings = set()        # Cache substrings that have appeared
    min_copy_length = min(1, b/a)   # At what length does it make sense to copy?
    for i in range(1, len(cost)):
        cost[i] = min(cost[i], cost[i-1] + a)
        # j <= i:            You can't copy more than you have already built
        # i + j < len(cost): You can't copy more than length of string
        # s[i:i+j] in s[:i]: The future string appears in the current one 
        j = min_copy_length
        while (j <= i and i + j < len(cost)):
            if s[i:i+j] not in found_substrings and s[i:i+j] in s[:i]:
                found_substrings.add(s[i:i+j])
            else:
                break
            cost[i+j] = min(cost[i+j], cost[i] + b)
            j += 1
    return cost[-1]

def build_string_dp(a, b, s):
    """ Finds the lowest cost to build a string using DP """
    cost = [0] + ([2**31 - 1] * len(s))
    min_copy_length = min(1, b/a)   # At what length does it make sense to copy?
    for i in range(1, len(cost)):
        cost[i] = min(cost[i], cost[i-1] + a)
        # j <= i:            You can't copy more than you have already built
        # i + j < len(cost): You can't copy more than length of string
        # s[i:i+j] in s[:i]: The future string appears in the current one 
        j = min_copy_length
        while (j <= i and i + j < len(cost) and s[i:i+j] in s[:i]):
            cost[i+j] = min(cost[i+j], cost[i] + b)
            j += 1
    return cost[-1]

def build_string(a, b, s):
    """
    Finds the lowest cost of making a string given
    append cost a, substring copy cost b, and target string s
    """
    # specify which version you want to use
    # DP, DP_MEMO, SUFFIX, RABIN_KARP
    VERSION = "DP"
    # func_map = {
    #     "DP": build_string_dp,
    #     "DP_MEMO": build_string_dp_memo,
    #     "SUFFIX": build_string_suffix,
    #     "RABIN_KARP": build_string_rabin_karp
    # }
    # return map(func_map[VERSION], (a, b, s))
    if VERSION == "DP":
        # the "most working" version
        return build_string_dp(a, b, s)
    elif VERSION == "DP_MEMO":
        return build_string_dp_memo(a, b, s)
    elif VERSION == "SUFFIX":
        # this one only passes 3 test cases, pls don't use (yet)
        return build_string_suffix(a, b, s)
    elif VERSION == "RABIN_KARP":
        return build_string_rabin_karp(a, b, s)


if __name__ == '__main__':
    print build_string(4, 5, 'aabaacaba')  # 26
    print build_string(8, 9, 'bacbacacb')  # 42


# Ignore everything below this line


# THIs Is FOR HACKERRANK
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     t = int(raw_input())

#     for t_itr in xrange(t):
#         nab = raw_input().split()

#         n = int(nab[0])

#         a = int(nab[1])

#         b = int(nab[2])

#         s = raw_input()

#         result = buildstring(a, b, s)
#         fptr.write(str(result) + "\n")

#     fptr.close()
