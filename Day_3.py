# Problem: Palindrome After Cleanup
# Link: https://www.hackerrank.com/contests/classroomtech-coding-contest/challenges/palindrome-after-cleanup/submissions/code/1394831270
# Author: Joydeep Garai
# Language: Python 3

str = input()
final_str = ""
for char in str:
    if char.isalnum():
        final_str += char.lower()
if final_str == final_str[::-1]:
    print("YES")
else:
    print("NO")