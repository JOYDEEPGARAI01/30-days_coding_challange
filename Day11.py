#Longest Common Subsequence (LCS) of Two Strings

A = input().strip()
B = input().strip()

n = len(A)
m = len(B)

prev_str = [0] * (m + 1)

for i in range(1, n + 1):
    curr_str = [0] * (m + 1)
    for j in range(1, m + 1):
        if A[i - 1] == B[j - 1]:
            curr_str[j] = prev_str[j - 1] + 1
        else:
            curr_str[j] = max(prev_str[j], curr_str[j - 1])
    prev_str = curr_str

print(prev_str[m])