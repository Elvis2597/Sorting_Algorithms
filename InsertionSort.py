#Time Complexity: O(n*n)
def insertionSort(l):
    for i in range(1, len(l)):
        element = l[i]
        j = i-1
        while j >=0 and element < l[j] :
                l[j+1] = l[j]
                j -= 1
        l[j+1] = element
    return l

l=list(map(int,input().split()))
print(insertionSort(l))
