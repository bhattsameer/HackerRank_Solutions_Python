#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the birthdayCakeCandles function below.
#
def birthdayCakeCandles():
    age = int(raw_input())
    candles = map(int, raw_input().rstrip().split())
    
    m = max(candles)
    c = candles.count(m)
    return c

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    result = birthdayCakeCandles()

    f.write(str(result) + '\n')

    f.close()
