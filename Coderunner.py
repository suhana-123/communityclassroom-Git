data = list(map(int, input().split(" ")))
l = []
for i in range(len(data)):
    count=0
    for j in range(len(data)):
        x=[]
        
        if data[i]==data[j]:
            count=count+1
        
    if tuple([data[i],count]) not in l:
        l.append(tuple([data[i],count]))
print(l)
