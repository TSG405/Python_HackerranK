'''
Problem Statement: https://www.hackerrank.com/challenges/pangrams/problem
@Coded by TSG, 2021
'''


import math
import os
import random
import re
import sys

d = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}

def pangrams(s):
    
    for tt in list(s.lower()):
        d[tt]=d.get(tt,0) + 1
    for key in d:
        if d[key] == 0:
            return ('not pangram')
    return ('pangram')

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
    
    
