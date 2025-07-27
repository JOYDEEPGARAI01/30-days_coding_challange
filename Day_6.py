# Remove duplicates from an array
# Link:https://www.hackerrank.com/contests/classroomtech-coding-contest/challenges/remove-duplicates-from-an-array-5-1/submissions/code/1394939902
# Author: Joydeep Garai
# Language: Python 3

n = int(input())
arr = list(map(int,input().split()))
uniq_elm = []
for i in range(n):
    if arr[i] not in uniq_elm:
        uniq_elm.append(arr[i])
for num in uniq_elm:
    print(num,end=" ")