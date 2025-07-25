# Problem: GCD of Multiple Numbers in a List
# Link: https://www.hackerrank.com/contests/classroomtech-coding-contest/challenges/gcd-of-multiple-numbers-in-a-list/submissions/code/1394886235
# Author: Joydeep Garai
# Language: Python 3

def find_gcd(a,b):
    while b!=0:
        a,b = b,a%b
    return a
n = int(input())
integers = list(map(int,input().split( )))
result = integers[0]
for i in range(1,n):
    result = find_gcd(result,integers[i])
print(result)