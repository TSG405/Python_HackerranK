'''
Problem Statement: https://www.hackerrank.com/challenges/the-time-in-words/problem
@Coded by TSG, 2020
'''

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
def timeInWords(h, m):
    res = ''
    numbers = ['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve', 'thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty']
    minute = 'minute'
    
    if m != 1:
        minute += 's'
        
    if m == 0:
        res = numbers[h] + " o' clock"
    elif m == 30:
        res = "half past " + numbers[h]
    elif m == 15:
        res = "quarter past " + numbers[h]
    elif m == 45:
        res = "quarter to " + numbers[h + 1]
    elif m < 20:
        res = numbers[m] + ' ' + minute + ' past ' + numbers[h]
    elif m < 30:
        res = numbers[-1] + ' ' + numbers[int(m%10)] + ' ' + minute + ' past ' + numbers[h]
    elif m > 45:
        res = numbers[60 - m] + ' ' + minute + ' to ' + numbers[h + 1]
    elif m > 30:
        res = numbers[-1] + ' ' + numbers[int(m%10)] + ' ' + minute + ' to ' + numbers[h + 1]
    
    return res.replace('  ', ' ')
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
