
N = int(input())
w = [0]*(N+1)
A = [0]*(N+1)
for i in range(1,N+1):
    w[i] = int(input())
A[0] = 0
A[1] = w[1]

for i in range(2,N+1):
    A[i] = max(A[i-1],A[i-2]+w[i])
#    print(A[i],A[i-1],A[i-2],w[i])
i = N
s = []
while i >= 1:
    if A[i-1]>=A[i-2]+w[i]:
        i-=1
    else:
        s.append(i)
        i-=2

print(s)
