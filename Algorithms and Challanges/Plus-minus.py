#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the plusMinus function below.
#
def plusMinus():
    n=float(raw_input())
    numbers=map(int,raw_input().split())
    print(round(len([i for i in numbers if i>0])/n,3))
    print(round(len([i for i in numbers if i<0])/n,3))
    print(round(len([i for i in numbers if i==0])/n,3))
            

if __name__ == '__main__':
    plusMinus()
