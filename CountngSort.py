#Time Complexity: O(n+k) where n is the number of elements in input array and k is the range of input.
def countingsort(l):
    count = [0 for i in range(max(l)+1)]
    #count array to store count of each unique element
    for i in l:
        count[i] += 1 
    #Modify the count array such that it stores the sum of previous one
    for j, el in enumerate(count):
        if j > 0:
            count[j] = count[j-1] + count[j]

    a= [0 for i in range(len(l)+1)]
    for k in l:
        ind = count[k]
        a[ind] = k
        count[k] -= 1 

    return a[1:] 
        
print(counting([27, 4, 15, 9, 110, 0, 13, 25, 1, 17, 802, 66, 25, 45, 97, 9]))

