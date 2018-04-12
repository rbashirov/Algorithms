from collections import defaultdict

if __name__ == '__main__':
    N_v, N_e = map(int, input().split())
    Vert = set()
    X = set()
    graph = []
    e = []
    for n in range(N_e):
        graph.append(input().split())

    dGraph = defaultdict(dict)
    for a,b,r in graph:
        dGraph[a][b] = r
        dGraph[b][a] = r
        Vert.add(a)
        Vert.add(b)

    Vert.remove('1')
    X.add('1')
    sum = 0

    while len(Vert) > 0:
        min = False
        for i in X:
            for j in Vert:
                if min == False:
                    try:
                        min = int(dGraph[i][j])
                        new_e = j
                    except:
                        pass
                else:
                    try:
                        if int(dGraph[i][j]) < min:
                            min = int(dGraph[i][j])
                            new_e = j
                    except:
                        pass
        Vert.remove(new_e)
        X.add(new_e)
        sum+=min

    print(sum)
