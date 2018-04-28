from collections import defaultdict

class UF:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1 for x in range(n)]
        self.group = defaultdict(list)
        for i in range(n): self.group[i] = [i]

    def find(self, v):
        return self.parent[v]

    def union(self, x, y):
        xRoot = self.find(x)
        yRoot = self.find(y)
        if xRoot == yRoot:
            return
        if self.rank[xRoot] > self.rank[yRoot]:
            for i in self.group[yRoot]: self.parent[i] = xRoot
            self.rank[xRoot] += self.rank[yRoot]
            self.rank[yRoot] = 0
            self.group[xRoot]+=self.group[yRoot]
            self.group[yRoot] = []
        else:
            for i in self.group[xRoot]: self.parent[i] = yRoot
            self.rank[yRoot] += self.rank[xRoot]
            self.rank[xRoot] = 0
            self.group[yRoot]+=self.group[xRoot]
            self.group[xRoot] = []

    def printParent(self):
        #print("index: ",list(range(9)))
        print("parent: ", self.parent, sep='')

def custom_s(s):
    return s[1]

if __name__ == "__main__":
    N = int(input())
    uf = UF(N)
    r = []
    r_n = []
    graph = []
    count = 0
    dGraph = []
    while True:
        try:
            p, q , r_t = map(int,input().split())
            r.append(r_t)
            dGraph.append([p-1,q-1,r_t])
            count+=1
        except:
            break
    for i,j in enumerate(r):
        r_n.append([i,j])
    r_n.sort(key=custom_s)
    c=0

    clustering = 4

    while True:
        uf.union(dGraph[r_n[c][0]][0], dGraph[r_n[c][0]][1])
        if len(set(uf.parent)) == clustering - 1:
            break
        c+=1
    uf.printParent()
    print(set(uf.parent))
    print(r_n[c][1])
