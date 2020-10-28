'''
Problem Statement: https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem
@Coded by TSG,2020
'''

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    count=0
    for l in range(i,j+1):
        n = (str(l)[::-1])
        if(abs(l-int(n))%k ==0):
            count+=1
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
