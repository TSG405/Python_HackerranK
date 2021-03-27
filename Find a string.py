'''
Problem Statement: https://www.hackerrank.com/challenges/find-a-string/problem
@Coded by TSG,2021
'''


def count_substring(string, sub_string):
    c=0 
    k = len(sub_string) 
    for i in range(len(string)-k+1):
        if string[i:k+i]==sub_string[:]:
            c+=1
    return c

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
