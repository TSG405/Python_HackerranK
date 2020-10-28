'''
Problem Statement: https://www.hackerrank.com/challenges/no-idea/problem
@Coded by TSG, 2020
'''

n, m = input().split()

array = input().split()
A = set(input().split())
B = set(input().split())

print(sum([(i in A) - (i in B) for i in array]))
