'''
Problem Statement: https://www.hackerrank.com/challenges/queens-attack-2/problem
@Coded by TSG, 2020
'''

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, qr, qc , obs):
    closet_row_obs_left = 1
    closet_row_obs_right = n
    closet_col_obs_up = n
    closet_col_obs_down = 1
    dai_obs_ur_qr = qr
    dai_obs_ur_qc = qc
    dai_obs_ul_qr = qr
    dai_obs_ul_qc = qc
    dai_obs_dl_qr = qr
    dai_obs_dl_qc = qc
    dai_obs_dr_qr = qr
    dai_obs_dr_qc = qc
    dai_ur = True
    dai_ul = True
    dai_dr = True
    dai_dl = True
    for x in obs:
        if x[0] == qr:
            t_obs_l = x[1]
            if t_obs_l >= closet_row_obs_left and t_obs_l <= qc:
                closet_row_obs_left = t_obs_l+1
            t_obs_r = x[1]
            if t_obs_r <= closet_row_obs_right and t_obs_r >= qc:
                closet_row_obs_right = t_obs_r-1
        if x[1] == qc:
            t_obs_up = x[0]
            if t_obs_up <= closet_col_obs_up and t_obs_up >= qr:
                closet_col_obs_up = t_obs_up-1
            t_obs_down = x[0]
            if t_obs_down >= closet_col_obs_down and t_obs_down <= qr:
                closet_col_obs_down = t_obs_down+1
        #for dai_ur
        if x[0] > qr and x[0] <= n and x[1] > qc and x[1] <= n:
            if (x[0]-qr+1) == (x[1]-qc+1):
                t_ur_qr = n-x[0]+qr+1
                t_ur_qc = n-x[1]+qc+1
                if dai_ur:
                    dai_obs_ur_qr = n-x[0]+qr+1
                    dai_obs_ur_qc = n-x[1]+qc+1
                    dai_ur = False
                elif t_ur_qc > dai_obs_ur_qr and t_ur_qc > dai_obs_ur_qc:
                    dai_obs_ur_qr = t_ur_qr
                    dai_obs_ur_qc = t_ur_qc
        #for dai_ul
        if x[0] > qr and x[0] >= 1  and x[1] < qc and x[1] >= 1:
            if (x[0]-qr+1) == -(x[1]-qc-1):
                t_ul_qr = qr-x[0]
                t_ul_qc = qc-x[1]
                if dai_ul:
                    dai_obs_ul_qr = qr-x[0]
                    dai_obs_ul_qc = qc-x[1]
                    dai_ul = False
                if t_ul_qr > dai_obs_ul_qr and t_ul_qc < dai_obs_ul_qc:
                    dai_obs_ul_qr = t_ul_qr
                    dai_obs_ul_qc = t_ul_qc
        #for dai_dr
        if x[0] < qr and x[0] >= 1 and x[1] > qc and x[1] <= n:
            if -(x[0]-qr-1) == (x[1]-qc+1):
                t_dai_qr = qr-x[0]
                t_dai_qc = x[1]-qc
                if dai_dr:
                    dai_obs_dr_qr = qr-x[0]
                    dai_obs_dr_qc = x[1]-qc
                    dai_dr = False
                elif t_dai_qr < dai_obs_dr_qr and t_dai_qc < dai_obs_dr_qc:
                    dai_obs_dr_qr = qr-x[0]
                    dai_obs_dr_qc = x[1]-qc
        #for dai_dl
        if x[0] < qr and x[0] >= 1 and x[1] < qc and x[1] >= 1:
            if -(x[0]-qr-1) == -(x[1]-qc-1):
                t_dl_qr = qr-x[0]
                t_dl_qc = qc-x[1]
                if dai_dl:
                    dai_obs_dl_qr = qr-x[0]
                    dai_obs_dl_qc = qc-x[1]
                    dai_dl = False
                if t_dl_qr < dai_obs_dl_qr and t_dl_qc < dai_obs_dl_qc:
                    dai_obs_dl_qr = qr-x[0]
                    dai_obs_dl_qc = qc-x[1]
    row_l = qc - closet_row_obs_left
    row_r = closet_row_obs_right - qc
    col_u = closet_col_obs_up - qr
    col_d = qr - closet_col_obs_down
    dai_ur = (n - max(dai_obs_ur_qr,dai_obs_ur_qc))
    dai_ul = min(n-dai_obs_ul_qr,dai_obs_ul_qc-1)
    dai_dr = min(dai_obs_dr_qr-1,n-dai_obs_dr_qc)
    dai_dl = min(dai_obs_dl_qr,dai_obs_dl_qc) - 1
    #print row_l, row_r, col_u, col_d, dai_ur, dai_ul, dai_dr, dai_dl
    return (row_l + row_r + col_u + col_d + dai_ur + dai_ul + dai_dr + dai_dl)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
