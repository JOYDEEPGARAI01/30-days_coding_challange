# Problem: Sort the Unsorted
# Link: https://www.hackerrank.com/classroomtech-coding-contest 
# Author: Joydeep Garai
# Language: Python 3
n = int(input())
array = list(map(int,input().split()))
array.sort()
print(*array)