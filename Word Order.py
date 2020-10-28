'''
Problem Statement: https://www.hackerrank.com/challenges/word-order/problem
@Coded by TSG, 2020
'''

from collections import OrderedDict

dict = OrderedDict()

for _ in range(int(input())):
    key = input()
    dict[key] = dict.get(key, 0) + 1

print(len(dict))
print(*dict.values())
