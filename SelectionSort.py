#Time Complexity = O(n^2)
def selection(l):
    for i in range(len(l)):
        #initializing the ith element of the list as min
        min_n=i
        #loop to find the minimum element in the list
        for j in range(i+1,len(l)):
            if l[j]<l[min_n]:
                min_n=j
        #swaping the minimum element with ith element
        l[i],l[min_n]=l[min_n],l[i]
    return l

l=list(map(int,input().split()))
print(selection(l))
