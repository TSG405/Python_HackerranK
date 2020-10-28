'''
Problem Statement: https://www.hackerrank.com/challenges/absolute-permutation/problem
@Coded by TSG, 2020
'''

import math
import os
import random
import re
import sys

# Complete the absolutePermutation function below.
def absolutePermutation(n, k):
    out = []
    switch = k
    if k == 0:
        return [x for x in range(1, n+1)]
    
    if n % (2*k) != 0:
        return [-1]
        
    for pos in range(1, n + 1):
        out.append(pos + switch)
        
        if pos % k == 0:
            switch *= -1
            
    return out
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
