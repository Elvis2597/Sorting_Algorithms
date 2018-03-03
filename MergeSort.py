#Time Complexity = O(nlogn)

#Function to merge to array
def merge(a,l,r):
    nl=len(l)
    nr=len(r)
    i=0
    j=0
    k=0
    while (i<nl and j<nr):
        if l[i]<=r[j]:
            a[k]=l[i]
            i+=1
        else:
            a[k]=r[j]
            j+=1
        k+=1
    while (i<nl):
        a[k]=l[i]
        i+=1
        k+=1
    while (j<nr):
        a[k]=r[j]
        j+=1
        k+=1

#main Function which calls the merge function to perform mergesort
def mergesort(a):
    n=len(a)
    if n<2:
        return
    mid=n//2
    l= a[:mid]
    r= a[mid:]
    mergesort(l)
    mergesort(r)
    merge(a,l,r)
    return a
l=list(map(int,input().split()))
print(mergesort(l))
