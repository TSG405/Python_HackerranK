'''
Problem Statement: https://www.hackerrank.com/challenges/pangrams/problem
@Coded by TSG, 2021
'''

import math
import os
import random
import re
import sys

def camelcase(s):
    c=0
    for tt in list(s):
        if tt.isupper():
            c=c+1
    return (c+1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
