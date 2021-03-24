'''
Problem Statement: https://www.hackerrank.com/challenges/between-two-sets/problem
@Coded by TSG, 2021
'''


#!/bin/python3

import math
import os
import random
import re
import sys
from math import gcd


def get_hcf(arr):
    hcf = arr[0] 
    for i in arr:
        hcf = gcd(hcf,i)
    return hcf

def lcm(a,b):
    return a*b//gcd(a,b)

def get_lcm(arr):
    l = arr[0] 
    for i in arr:
        l = lcm(l,i)
    return l

def getTotalX(a, b):
    lcm_a = get_lcm(a)
    hcf_b = get_hcf(b)
    f = [i for i in range(lcm_a, hcf_b+1) if not hcf_b%i and not i%lcm_a]
    return(len(f))
        
    
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))
    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')
    fptr.close()
