W, T = map(int,input().split())
v = [0]*T
w = [0]*W
A = [[0 for x in range(W+1)] for y in range(2)]
for i in range(T):
     tmp = list(map(int,input().split()))
     v[i] = tmp[0]
     w[i] = tmp[1]

for i in range(1,T+1):
    count=0
    for x in range(W+1):
        if x-w[i-1] >= 0:
            A[1][x] = max(A[0][x], A[0][x-w[i-1]]+v[i-1])
            count = 1
        else:
            A[1][x] = A[0][x]
    if count == 1:
        for j in range(len(A[0])):
            A[0][j] = A[1][j]
print(A[0][W])
