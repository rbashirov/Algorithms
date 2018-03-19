from heapq import *

def solution(A):
    medians = [0]*len(A)
    medians[0], medians[1] = A[0], min(A[0],A[1])
    h=[1]
    heap_l, heap_h  = [(-1)*min(A[0],A[1])], [max(A[0],A[1])]
    heapify(heap_l)
    heapify(heap_h)
    odd = True

    for i in range(2,len(A)):
        if odd == True:
            three = [A[i],(-1)*heappop(heap_l), heappop(heap_h)]
            three.sort()
            heappush(heap_l, (-1)*three[0])
            heappush(heap_l, (-1)*three[1])
            heappush(heap_h, three[2])
            medians[i]=(-1)*heap_l[0]
            odd=False
        else:
            three = [A[i],(-1)*heappop(heap_l), heappop(heap_h)]
            three.sort()
            heappush(heap_l, (-1)*three[0])
            heappush(heap_h, three[1])
            heappush(heap_h, three[2])
            medians[i]=(-1)*heap_l[0]
            odd = True

    return sum(medians)


if __name__ == '__main__':
    with open('Median.txt', 'r') as f:
        A = [int(line.strip()) for line in f]
    print(solution(A))
