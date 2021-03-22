'''
Problem Statement: https://www.hackerrank.com/challenges/permutation-equation/problem
@Coded by TSG,2021
'''

import math
import os
import random
import re
import sys

k=[]
def permutationEquation(p,n):
    for i in range (1,n+1):
        k.append(p.index(p.index(i)+1)+1)
    return(k)
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p,n)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
