'''
Problem Statement: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
@Coded by TSG,2020
'''

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    f=arr[0]
    for i in range(1,n):
        if arr[i]!=f:
            print(arr[i])
            break
