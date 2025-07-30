#Matrix Multiplication

p,q,r = map(int,input().split())
A = []
for i in range(p):
    row = list(map(int,input().split()))
    A.append(row)
B = []
for i in range(q):
    row = list(map(int,input().split()))
    B.append(row)
C = []
for i in range(p):
    row = [0] * r
    C.append(row)
for i in range(p):
    for j in range(r):
        for k in range(q):
            C[i][j] += A[i][k] * B[k][j]
for i in range(p):
    for j in range(r):
        print(C[i][j],end=" ")
    print()

