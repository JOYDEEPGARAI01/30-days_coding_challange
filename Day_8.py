# Merge 
#Second Distinct Largest Element in an Array
# Link:https://www.hackerrank.com/contests/classroomtech-coding-contest/challenges/second-distinct-largest-element-in-an-array/submissions/code/1395057011
# Author: Joydeep Garai
# Language: Python 3

n=int(input())
arr= list(map(int,input().split()))
final_arr = list(set(arr))
if len(final_arr)<2:
    print("NO")
else:
    final_arr.sort(reverse=True)
print(final_arr[1])
