def weighted_a(w,l):
    res = 0
    l_w = [0]*len(w)
    count = 0
    for i in range(len(w)):
        count+=l[i]
        l_w[i]=count
    for i in range(len(w)):
        res+=w[i]*l_w[i]
    return res

def custom_s(s):
    return s[1]+s[2]/10000

if __name__ == '__main__':
    T = int(input())
    w, l = [0]*T, [0]*T
    D, F = [0]*T, [0]*T
    F_s = []
    D_s = []
    w_s, l_s = [0]*T, [0]*T

    for n in range(T):
        w[n], l[n] = map(int, input().split())
        D[n] = w[n] - l[n]
        F[n] = w[n]/l[n]

    for num, Dif in enumerate(D):
        D_s += [(num,Dif,w[num])]
    for num, Frac in enumerate(F):
        F_s += [(num,Frac,w[num])]

    D_s.sort(key=custom_s)
    F_s.sort(key=lambda x: (x[1], not x[0]))

    for i in range(T-1):
        if D_s[i] == D_s[i+1]:
            if w[D_s[i][0]] > w[D_s[i+1][0]]:
                tmp = D_s[i]
                D_s[i] = D_s[i+1]
                D_s[i+1] = tmp

    for i in range(T):
        w_s[i] = w[D_s[T-1-i][0]]
        l_s[i] = l[D_s[T-1-i][0]]
    print(weighted_a(w_s,l_s))

    for i in range(T):
        w_s[i] = w[F_s[T-1-i][0]]
        l_s[i] = l[F_s[T-1-i][0]]
    print(weighted_a(w_s,l_s))
