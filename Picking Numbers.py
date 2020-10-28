'''
Problem Statement: https://www.hackerrank.com/challenges/picking-numbers/problem
@Coded by TSG, 2020
'''

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(arr):
    arr_s = sorted(arr)
    res = 1
    cur = 1
    diff = 0
    for ind in range(1, len(arr_s)):
       
        diff += arr_s[ind] - arr_s[ind - 1]
        if diff > 1:
            res = max(res, cur)
            cur = 1
            diff = 0
        else:
            cur += 1
            
    res = max(res, cur)
    
    return res
        
            # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
