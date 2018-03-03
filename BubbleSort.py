#Time Complexity = O(n^2)
#Time Complexity(best Case)= O(n)
def bubbleSort(l):
    for j in range(len(l)):
        #to keep track of swap
        flag=False
        #loop to compare the elements 
        for i in range(len(l)-1):
            if l[i]>l[i+1]:
                #swap the elements
                l[i],l[i+1]=l[i+1],l[i]
                flag=True
        #No swap then our list is sorted and we exit the loop
        if flag==False:
            break
    return l

l=list(map(int,input().split()))
print(bubbleSort(l))
                
                
