'''
Problem Statement: https://www.hackerrank.com/challenges/extra-long-factorials/problem
@Coded by TSG, 2020
'''

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    ans=1
    while(n!=1):
        ans*=n
        n-=1
    print (ans)
if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)
