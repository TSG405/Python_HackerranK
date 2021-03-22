'''
Problem Statement: https://www.hackerrank.com/challenges/the-hurdle-race/problem
@Coded by TSG,2021
'''


import math
import os
import random
import re
import sys


def hurdleRace(k, height):
    return max(0,max(height)-k)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    height = list(map(int, input().rstrip().split()))
    result = hurdleRace(k, height)

    fptr.write(str(result) + '\n')
    fptr.close()
