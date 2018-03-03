#Time Complexity of Heap Sort is O(nLogn).
#heapify the array
def heap(l,n,i):
    large=i
    #left child
    left=2*i + 1
    #right child
    right=2*i + 2
    #left child is greater than root
    if left<n and l[large]<l[left]:
        large=left
    #right child is greater than root
    if right<n and l[large]<l[right]:
        large=right
    #swap the root
    if large != i:
        l[i],l[large] = l[large],l[i]  
        # Heapify the root.
        heap(l, n, large)

#main Function 
def heapsort(l):
    for i in range(len(l),-1,-1):
        heap(l,len(l),i)    #maxheap
    for i in range(len(l)-1,0,-1):
        l[i],l[0]=l[0],l[i]
        heap(l,i,0)
    return l
#Taking the input
l=list(map(int,input().split()))
print(heapsort(l))
