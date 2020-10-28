'''
Problem Statement: https://www.hackerrank.com/challenges/bigger-is-greater/problem
@Coded by TSG, 2020
'''

import math
import os
import random
import re
import sys

# Complete the biggerIsGreater function below.
def swap_characters(s, i, j):
    lst = list(s);
    lst[i], lst[j] = lst[j], lst[i]
    return ''.join(lst)


def reverse_substring(s, i, j):
    return s[:i] + s[i:j][::-1] + s[j:]
def biggerIsGreater(initial_string):
    index_of_first_element_to_swap = 0
    for i in range(1, len(initial_string)):
        if initial_string[i] > initial_string[i - 1]:
            index_of_first_element_to_swap = i
    if index_of_first_element_to_swap == 0:
        return "no answer"
    else:

        # b)
        index_of_second_element_to_swap = 0
        for j in range(index_of_first_element_to_swap, len(initial_string)):
            if initial_string[j] > initial_string[index_of_first_element_to_swap - 1]:
                index_of_second_element_to_swap = j

        # c)
        string_with_swapped_characters = swap_characters(initial_string, index_of_first_element_to_swap - 1,
                                                         index_of_second_element_to_swap)

        # d)

        final_string = reverse_substring(string_with_swapped_characters, index_of_first_element_to_swap,
                                         len(initial_string))


        return final_string
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
