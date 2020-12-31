'''
Problem Statement: https://www.hackerrank.com/challenges/balanced-brackets/problem
@Coded by TSG, 2020
'''

open_list = ["[","{","("] 
close_list = ["]","}",")"]

import math
import os
import random
import re
import sys

open_list = ["[","{","("] 
close_list = ["]","}",")"]

# Driver Function
def isBalanced(s):
    global open_list
    global close_list
    
    stack = [] 
    
    for i in (s): 
        if i in (open_list): 
            stack.append(i) 
        elif i in (close_list): 
            pos = close_list.index(i) 
            if ((len(stack) > 0) and (stack[len(stack)-1]) == open_list[pos]): 
                stack.pop() 
            else: 
                return ("NO")              
    if len(stack) == 0: 
        return ("YES")
    else:
        return ("NO")
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
