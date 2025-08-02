#Find First Non-Repeating Character in a String
S = input()
count_dict = {}
for char in S:
    if char in count_dict:
        count_dict[char] += 1
    else:
        count_dict[char] = 1
found = False
for char in S:
    if count_dict[char] == 1:
        print(char)
        found = True
        break
if not found:
    print("NO")