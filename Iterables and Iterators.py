'''
Problem Statement: https://www.hackerrank.com/challenges/iterables-and-iterators/problem
@Coded by TSG, 2020
'''

from itertools import combinations

n = int(input())
array = input().split()
k = int(input())

comb_list = list(combinations(array, k))
a_list = [e for e in comb_list if 'a' in e]
print(len(a_list) / len(comb_list))
