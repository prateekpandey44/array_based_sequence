def insertion_sort(A):
    """sort list of compariable element into non decending order"""
    for k in range(1,len(A)):
        cur = A[k]
        j=k
        while j>0 and a[j-1]>cur:
            A[j]=A[j-1]
            j-=1
        A[j]=cur