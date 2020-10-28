'''
Problem Statement: https://www.hackerrank.com/challenges/circular-array-rotation/problem
@Coded by TSG, 2020
'''

import math
import os
import random
import re
import sys

# Complete the circularArrayRotation function below.
def circularArrayRotation(a, k, queries):
    n=len(a)
    re=k%n
    temp=a[:n-(re)]
    temp1=a[n-(re):]
    nf=temp1+temp
    f=[]
    for tt in queries:
        f.append(nf[tt])
    return(f)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nkq = input().split()

    n = int(nkq[0])

    k = int(nkq[1])

    q = int(nkq[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
