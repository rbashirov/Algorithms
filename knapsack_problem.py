W, T = map(int,input().split())
v = [0]*T
w = [0]*W
A = [[0 for x in range(W+1)] for y in range(T+1)]
for i in range(T):
     tmp = list(map(int,input().split()))
     v[i] = tmp[0]
     w[i] = tmp[1]
     print(w[i])
for i in range(1,T+1):
    for x in range(W+1):
        if x-w[i-1] >= 0:
            A[i][x] = max(A[i-1][x], A[i-1][x-w[i-1]]+v[i-1])
        else:
            A[i][x] = A[i-1][x]
print(A[T][W])
