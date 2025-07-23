# Problem: Find the target(Binary search)
# Link: https://www.hackerrank.com/contests/classroomtech-coding-contest/challenges/find-the-target-binary-search/submissions/code/1394760528
# Author: Joydeep Garai
# Language: Python 3
n = int(input())
arr = list(map(int,input().split()))
target = int(input())
low_elm = 0
high_elm = n-1
result = -1
while low_elm <= high_elm:
    mid_elm = (low_elm + high_elm) // 2
    if arr[mid_elm] == target:
        result = mid_elm  
        break         
    elif arr[mid_elm] < target:
        low_elm = mid_elm + 1  
    else:
        high_elm = mid_elm - 1 
print(result)