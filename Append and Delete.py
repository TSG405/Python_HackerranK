'''
Problem Statement: https://www.hackerrank.com/challenges/append-and-delete/problem
@Coded by TSG,2020
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.

def appendAndDelete(s, t, k):
    S=list(s)
    T=list(t)
    
    m,mm=len(S),len(T)
    min_len=min(m,mm)
    
    c = min_len

    for i in range(c):
        if S[i] != T[i]:
            break
    c=i
    op = m + mm - (2 * c)

    if ((k == op) or (k >= len(s) + len(t)) or (k >= op and (k - op) % 2 == 0)):
        return ("Yes") 
    
    else:
        return("No")



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    t = input()
    k = int(input())

    result = appendAndDelete(s, t, k)
    
    fptr.write(result + '\n')
    fptr.close()
