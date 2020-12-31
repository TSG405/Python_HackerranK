'''
Problem Statement: https://www.hackerrank.com/challenges/equal-stacks/problem
@Coded by TSG, 2020
'''


import math
import os
import random
import re
import sys

# Driver function
def equalStacks(h1, h2, h3):
    l1, l2, l3 = sum(h1),sum(h2),sum(h3)
    
    while l1 != 0 and l2 != 0 and l3 != 0 and (l1!=l2 or l2!=l3):
        if max(l1, l2, l3) == l1:
            l1 = l1 - h1[0]
            h1.pop(0)
        elif max(l1, l2, l3) == l2:
            l2 = l2 - h2[0]
            h2.pop(0)
        else:
            l3 = l3 - h3[0]
            h3.pop(0)
            
    else:
        if l1==l2 and l2==l3:
            return l1
        else:
            return 0
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])
    
    
    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
