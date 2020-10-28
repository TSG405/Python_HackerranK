'''
Problem Statement: https://www.hackerrank.com/challenges/larrys-array/problem
@Coded by TSG, 2020
'''

import math
import os
import random
import re
import sys

# Complete the larrysArray function below.
def larrysArray(n,numbers):
    number_of_inversions = 0
        
    for i in range(0, n):
        for j in range(i + 1, n):
            if numbers[i] > numbers[j]:
                number_of_inversions += 1
    return ("YES" if number_of_inversions % 2 == 0 else "NO")
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(n,A)

        fptr.write(result + '\n')

    fptr.close()
