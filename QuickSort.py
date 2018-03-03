#Function for partition
def partition(l,start,end):
    #last element is selected as pivot
    pivot=l[end]
    #partition index is at start 
    pi=start
    for i in range(start,end):
        #comparing the pivot and ith element of list 
        if l[i]<=pivot:
            l[i],l[pi]=l[pi],l[i]
            #incrementing the partition index
            pi+=1
    #swapping the pivot element
    l[pi],l[end]=l[end],l[pi]
    return pi
#Main Function to do quicksort
def quicksort(l,start,end):
    if start<end:
        pi=partition(l,start,end)
        quicksort(l,start,pi-1)
        quicksort(l,pi+1,end)
    return l
#Taking input

l=list(map(int,input().split()))
print(quicksort(l,0,len(l)-1))
