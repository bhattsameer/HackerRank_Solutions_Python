#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the miniMaxSum function below.
#
def miniMaxSum():
    arr = map(int,raw_input().strip().split(' '))
    x = sum(arr)
    print (str((x-(max(arr))))+" "+str((x-(min(arr)))))

if __name__ == '__main__':
    miniMaxSum()
