'''
Problem Statement: https://www.hackerrank.com/challenges/maximize-it/problem
@Coded by TSG, 2020
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
k,m = map(int, input().split())
l = []
for i in range(k):
  l.append([x*x for x in list(map(int, input().split()))[1:]])
 
s = 0
for e in itertools.product(*l):
  temp = sum(e)%m
  if temp > s:
    s = temp
print(s)
