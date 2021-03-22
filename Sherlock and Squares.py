'''
Problem Statement: https://www.hackerrank.com/challenges/sherlock-and-squares/problem
@Coded by TSG,2021
'''


import math
import os
import random
import re
import sys

def squares(a, b):
    c=0
    s = int(a**0.5)        
    k=s+(s+1)
    r = s**2                 # nearest perfect square (lower)
    while(r<=b):             # nearest integer root adds up with it's immediate next integer to generate the difference between consecutive squares. N.B -- The difference adds up by '2' every time.
        r+=k                 # The series -- "1 4 9 16 25" have "3 5 7 9" differences respectively. So taking  any number, and finding it's nearest square (lower bounded) adds up to its root and it's neighbour, to find the next square number.Then the differences continue to add '2' to it!
        if r>b:
            break
        else:
            k+=2  
            c+=1
    if (r >= a):
        return(c+1)
    else:
        return (c)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])
        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')
    fptr.close()
