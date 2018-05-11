#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    temp = 0 
    for i in ar:
        temp = temp + i
    return temp
