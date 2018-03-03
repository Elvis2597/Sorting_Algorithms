#n=list(map(int,input().split()))
n=[0.78,0.17,0.39,0.26,0.72,0.94,0.21,0.12,0.23,0.68]
l = [[] for i in range(len(n))]
print(l)
for i in range(len(n)):
    n1=int(n[i]*10)
    print(n1)
    l[n1].append(n[i])
    
for j in l:
    j.sort()
y=(sum(l,[]))
print(*y)


