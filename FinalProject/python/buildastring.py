#!/bin/python
import os
import sys

#
# Complete the buildString function below.
#
def buildString(A, B, S):
    cost = [0] + ([300000000] * len(S))
    copy_length = min(1, B/A)
    for i in range(1, len(cost)):
        cost[i] = min(cost[i], cost[i-1] + A)

        # while you are in range AND it makes sense to copy
        # AND you are able to copy, do it.
        j = copy_length
        while j <= i and i < len(cost) - j and S[i:i+j] in S[:i]:
            cost[i+j] = min(cost[i+j], cost[i] + B)
            j += 1

    return cost[-1]

if __name__ == '__main__':
    print buildString(4, 5, 'aabaacaba')
    print buildString(8, 9, 'bacbacacb')



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
