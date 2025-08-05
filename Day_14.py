#Sum of Elements in a Subarray (Prefix Sum)

n, q = map(int, input().split())
A = list(map(int, input().split()))

# Step 1: Build the prefix sum array
prefix = [0] * (n + 1)
for i in range(1, n + 1):
    prefix[i] = prefix[i - 1] + A[i - 1]

# Step 2: Answer each query in O(1) time
for _ in range(q):
    L, R = map(int, input().split())
    print(prefix[R] - prefix[L - 1])
