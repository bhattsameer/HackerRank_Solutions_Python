#!/bin/python

from __future__ import print_function

import os
import sys

def diagonalDifference(a):
    sum1 = 0
    sum2 = 0
    sum1 = sum(a[i][i] for i in range(n))
    sum2 = sum(a[i][n-i-1] for i in range(n))
    result = sum1 - sum2
    return abs(result)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    a = []

    for _ in xrange(n):
        a.append(map(int, raw_input().rstrip().split()))
        
    result = diagonalDifference(a)

    f.write(str(result) + '\n')

    f.close()
