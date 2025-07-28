# Merge Two Sorted Arrays
# Link:https://www.hackerrank.com/contests/classroomtech-coding-contest/challenges/merge-two-sorted-arrays-24/submissions/code/1394993406
# Author: Joydeep Garai
# Language: Python 3

n = int(input())
arr_1 = list(map(int,input().split()))
m = int(input())
arr_2 = list(map(int,input().split()))
result_arr = []
i=0
j=0
for _ in range(n+m):
    if i<n and j<m:
        if arr_1[i]<=arr_2[j]:
            result_arr.append(arr_1[i])
            i+=1
        else:
            result_arr.append(arr_2[j])
            j+=1
    elif i<n:
        result_arr.append(arr_1[i])
        i+=1
    elif j<m:
        result_arr.append(arr_2[j])
        j+=1
    
print(*result_arr)
        