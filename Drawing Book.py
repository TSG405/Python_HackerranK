'''
Problem Statement: https://www.hackerrank.com/challenges/drawing-book/problem
@Coded by TSG, 2020
'''

import os
import sys

#
# Complete the pageCount function below.
#

def get_open(page):
    return 1 + (page//2)

def pageCount(n, p):
    return min(get_open(p) - get_open(1), get_open(n) - get_open(p))    #
    # Write your code here.
    #

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
