'''
Problem Statement: https://www.hackerrank.com/challenges/non-divisible-subset/problem
@Coded by TSG, 2020
'''

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

import sys
from itertools import combinations

def check_array(k, arr):
    for el1 in arr:
        test_arr = list(arr)
        test_arr.remove(el1)
        
        for el2 in test_arr:
            if (el1 + el2) % k == 0:
                return False
    return True

def nonDivisibleSubset_brute(k, arr):
    if check_array(k, arr):
        return len(arr)
    
    best = 0
    for num in range(1, len(arr)):
        to_remove = list(combinations(arr, num))
        #print("to_remove = {}".format(to_remove))
        for option in to_remove:
            test_arr = list(arr)
            #print("test_arr = {}".format(test_arr))
            for el in option:
                test_arr.remove(el)

            if check_array(k, test_arr) == True:
                best = max(len(test_arr), best)

    return best

def nonDivisibleSubset(k, arr):
    resid_cnt = [0] * k
    
    for el in arr:
        resid_cnt[el%k] += 1
        
    res = min(1, resid_cnt[0])
    for ind in range(1, (k//2)+1):
        if ind != k - ind:
            res += max(resid_cnt[ind], resid_cnt[k - ind])
    
    if k % 2 == 0 and resid_cnt[int(k/2)] != 0:
        res += 1
    
    return res
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
