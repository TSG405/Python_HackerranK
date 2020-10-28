'''
Problem Statement: https://www.hackerrank.com/challenges/matrix-script/problem
@Coded by TSG, 2020
'''

import re

# Import original script
matrix = list()
for _ in range(int(input().split()[0])):
    matrix.append(list(input()))

# Rotate the matrix
matrix = list(zip(*matrix))

# Prep regex sample
sample = str()
for subset in matrix:
    for letter in subset:
        sample += letter

# Substitute invalid characters with a space
print(re.sub(r'(?<=\w)([^\w\d]+)(?=\w)', ' ', sample))
