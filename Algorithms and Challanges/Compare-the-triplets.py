#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the solve function below.
#
def solve(a0, a1, a2, b0, b1, b2):
    result = []
    ra0=ra1=ra2=rb0=rb1=rb2=0
    if a0 > b0:
        ra0 = 1
    if a1 > b1:
        ra1 = 1   
    if a2 > b2:
        ra2 = 1
    if a0 < b0:
        rb0 = 1
    if a1 < b1:
        rb1 = 1
    if a2 < b2:
        rb2 = 1
    if a0 == b0:
        r0 = 0
    if a1 == b1:
        r1 = 0
    if a2 == b2:
        r2 = 0
        
    suma = ra0+ra1+ra2
    sumb = rb0+rb1+rb2
    result.append(suma)
    result.append(sumb)
    
    return result

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    a0A1A2 = raw_input().split()

    a0 = int(a0A1A2[0])

    a1 = int(a0A1A2[1])

    a2 = int(a0A1A2[2])

    b0B1B2 = raw_input().split()

    b0 = int(b0B1B2[0])

    b1 = int(b0B1B2[1])

    b2 = int(b0B1B2[2])

    result = solve(a0, a1, a2, b0, b1, b2)

    f.write(' '.join(map(str, result)))
    f.write('\n')

    f.close()
