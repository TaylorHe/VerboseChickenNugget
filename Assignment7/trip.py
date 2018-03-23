"""
Name          : trip.py
Author        : Taylor He, Jacob Manzelmann, Thomas Osterman
Version       : Best
Date          : March 22, 2018
Description   : solves http://www.spoj.com/problems/TRIP by using
                longest common subsequence implemented with dynamic programming,
                and recursive backtracking to find all the solutions.
                Backtracking is memoized using a set()
"""
import sys



def lcs_dp(s1, s2, show_table=False):
    """Returns a tuple of values. Index 0 contains the length of the longest
    common subsequence, while index 1 contains the string. Uses bottom-up
    dynamic programming to improve performance."""
    m = len(s1)
    n = len(s2)
    c = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
            else:
                c[i][j] = max(c[i][j - 1], c[i - 1][j])

    results = set()
    backtrack(s1, s2, m, n, c, results, '')
    return sorted(list(results))

found = set()

def backtrack(s1, s2, m, n, c, results, curr):
    """Recursively backtracks table c, and appends to result
    set the final word. 
    """
    # Use memoization.
    if (curr, m, n) in found: return
    # Base case, add to results
    if m == 0 or n == 0:
        results.add(curr)
        return
    # If the upper-left are equal, then add to the word
    if s1[m-1] == s2[n-1]:
        curr = s1[m-1] + curr
        backtrack(s1, s2, m-1, n-1, c, results, curr)
        return
    # if left =/= top, then backtrack with greater
    if c[m][n-1] >= c[m-1][n]:
        backtrack(s1, s2, m, n-1, c, results, curr)
    if c[m][n-1] <= c[m-1][n]:
        backtrack(s1, s2, m-1, n, c, results, curr)

    found.add((curr, m, n))

def prettyprint(l):
    for item in l: print(item)
    print("")

if __name__=='__main__':
    num = input()
    num = int(num)
    while num:
        num -= 1
        s1 = input()
        s2 = input()
        results = lcs_dp(s1, s2)
        prettyprint(results)
