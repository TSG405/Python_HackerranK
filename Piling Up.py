'''
Problem Statement: https://www.hackerrank.com/challenges/piling-up/problem
@Coded by TSG, 2020
'''

from collections import deque
for _ in range(int(input())):
    flag = True
    input()
    d = deque(map(int, input().strip().split()))
    if (d[0] >= d[-1]):
        max = d.popleft()
    else:
        max = d.pop()
    while d:
        if (len(d) == 1):
            if (d[0] <= max):
                break
            else:
                flag = False
                break;
        else:
            if d[0] <= max and d[-1] <= max:
                if d[0] >= d[-1]:
                    max = d.popleft()
                else:
                   max = d.pop()
            elif d[0] <= max:
                max = d.popleft()
            elif d[-1] <= max:
                max = d.pop()
            else:
                flag = False
                break;

    if flag:
        print ("Yes")
    else:
        print ("No")
