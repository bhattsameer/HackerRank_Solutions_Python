#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the staircase function below.
#
def staircase():
    n = int(input())
    for i in range(n):
        print(" "*(n-i-1)+"#"*(i+1))

if __name__ == '__main__':
    staircase()
