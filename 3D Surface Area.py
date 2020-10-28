'''
Problem Statement: https://www.hackerrank.com/challenges/3d-surface-area/problem
@Coded by TSG, 2020
'''

import math
import os
import random
import re
import sys

# Complete the surfaceArea function below.
def surfaceArea(A):
    result = 2 * H * W
    for i in range(H):
        for j in range(W):
            # We initially add the surface of the four lateral areas of the current cube...
            result += A[i][j] * 4
            # ... and then we remove the unnecessary areas, according to the height of the adjacent cubes
            # already considered
            if i != 0:
                result -= 2 * min(A[i - 1][j], A[i][j])
            if j != 0:
                result -= 2 * min(A[i][j], A[i][j - 1])
    return (result)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    HW = input().split()

    H = int(HW[0])

    W = int(HW[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
