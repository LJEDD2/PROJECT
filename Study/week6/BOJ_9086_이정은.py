n = int(input())
s_list =[]
ans=[]

for i in range(n):
    s_list.append(input())
    ans.append([s_list[i][0],s_list[i][-1]])
    
for i in range(n):
    print(''.join(ans[i]))
