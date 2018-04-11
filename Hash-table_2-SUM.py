if __name__ == '__main__':
    with open('2-sum.txt', 'r') as f:
        A = [int(line.strip()) for line in f]
    D = {}
    S = set()
    for i in range(len(A)):
        D[A[i]] = 1
    for i in A:
        for j in [x for x in range(-10000, 10001) if x not in S]:
                try:
                    if D[j-i] == 1 and (j-i)!=i:
                        S.add(j)
                        break
                except:
                    pass
    print(len(S))
