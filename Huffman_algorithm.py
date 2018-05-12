import heapq
from collections import defaultdict
 
 
def Encode_fun(feq):
    heap = [[weight, [symbol, '']] for symbol, weight in feq.items()]

    heapq.heapify(heap)
    while len(heap) > 1:
        low = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in low[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [low[0] + hi[0]] + low[1:] + hi[1:])
    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

N = int(input())

feq = defaultdict(int)

for i in range(N):
    feq[i] = int(input())
    


# Huffman coding function 
huff = Encode_fun(feq)
print (huff)
print(len(huff[0][1]), len(huff[-1][1]))
