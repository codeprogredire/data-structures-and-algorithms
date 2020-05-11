'''
Merge Sort
'''

def mergeSort(A,start,end):
    if start<end:
        mid=(start+end)//2
        mergeSort(A,start,mid)
        mergeSort(A,mid+1,end)
        merge(A,start,mid,end)

def merge(A,start,mid,end):
    n1=mid-start+1
    n2=end-mid

    L=[0]*n1
    R=[0]*n2

    for i in range(n1):
        L[i]=A[start+i]
    for j in range(n2):
        R[j]=A[mid+1+j]

    i=0
    j=0
    k=start

    while i<n1 and j<n2:
        if L[i]<=R[j]:
            A[k]=L[i]
            i+=1
        else:
            A[k]=R[j]
            j+=1
        k+=1

    while i<n1:
        A[k]=L[i]
        i+=1
        k+=1

    while j<n2:
        A[k]=R[j]
        j+=1
        k+=1


A=list(map(int,input().split()))
mergeSort(A,0,len(A)-1)
print(A)
