'''
Problem Statement: https://www.hackerrank.com/challenges/reduced-string/problem
@Coded by TSG,2021
'''

import math
import os
import random
import re
import sys


def superReducedString(s):
    l = list(s)
    str1=''
    t=0
    while(len(l) - t > 1):
        if l[t] == l[t+1]:
            del(l[t])
            del(l[t])
            if t!=0:
                t=t-1
        else:
            t=t+1
                
    if len(l)>0:
        for uu in l:
            str1 += uu
        return(str1)
    else:
        return('Empty String')   
                   
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
