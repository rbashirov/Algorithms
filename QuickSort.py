def quicksort(A):
    if len(A) > 1:
        pivot = A[0]
        left = [elem for elem in A[1:] if elem < pivot]
        right = [elem for elem in A[1:] if elem >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)
    else:
        return A

if __name__ == '__main__':
    print (quicksort([7,6,5,5,5,5,4,3,2,1]))
