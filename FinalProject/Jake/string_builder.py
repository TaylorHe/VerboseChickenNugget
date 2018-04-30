#!/bin/python
import os
import sys
from difflib import SequenceMatcher

def longestSubstring(str1,str2):
 
    seqMatch = SequenceMatcher(None,str1,str2)

    match = seqMatch.find_longest_match(0, len(str1), 0, len(str2))

    if (match.size!=0):
      return len((str1[match.a: match.a + match.size]))
    else:
      return 0

def buildString(append, copy, string):
    size = len(string)
    print(string)
    if size == 0:
        return 0
    lcs = 0
    size -= 1
    found = False
    while size != -1:
        temp = longestSubstring(string[:size], string[size:])
        if temp <= lcs:
            if found:
                return min(copy, append * (len(string[size:]) - 1)) + buildString(append,copy,string[:size+1])
            print(min(copy, append * (len(string[size:]))))
            return min(copy, append * (len(string[size:]))) + buildString(append,copy,string[:size])
        lcs = temp
        size -= 1
        found = True

if __name__ == '__main__':
    print buildString(2, 5, "aabaacaba")
    print buildString(8, 9, "bacbacacb")
    print buildString(2709, 2712, "caackncaacknggikncaacknggaacknggikncaackggikncaacknggaacknggikncakqoaacknggikncacggih")