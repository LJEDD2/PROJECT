n = int(input())
A= list(map(int,input().split()))
result = sorted(A)
p=[]
for i in A:
    p.append(result.index(i))
    result[result.index(i)] = -1
    
print(*p)
