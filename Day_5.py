# Problem: Case-Insensitive Character Frequency with Sorting
# Link: https://www.hackerrank.com/contests/classroomtech-coding-contest/challenges/case-insensitive-character-frequency-with-sorting/submissions/code/1394917329
# Author: Joydeep Garai
# Language: Python 3

s = input()
frequency ={}
for char in s:
    if char != " "  and char.isalnum():
        char = char.lower()
        if char in frequency:
            frequency[char] +=1
        else:
            frequency[char] = 1
for key in sorted(frequency):
    print(f"{key} : {frequency[key]}")