def merge(A, B):
    # A = 1st sorted array [n/2]
    # B = 2nd sorted array [n/2]
    # C = output array [n]
    C=[]
    if len(A)==0:
        return B
    if len(B)==0:
        return A
    i,j = 0,0
    while len(C) < len(A) + len(B):
        if A[i] < B[j]:
            C.append(A[i])
            i+=1
        else:
            C.append(B[j])
            j+=1
        if i == len(A):
            C.extend(B[i:])
            break
        if j == len(B):
            C.extend(A[i:])
            break
    return C

def mergesort(I):
    if len(I)<=1:
        return I
    mid = int(len(I)/2)
    A = MergeSort(I[:mid])
    B = MergeSort(I[mid:])
    return merge(A,B)

if __name__ == '__main__':
    print (mergesort([7,6,5,5,5,5,4,3,2,1]))
