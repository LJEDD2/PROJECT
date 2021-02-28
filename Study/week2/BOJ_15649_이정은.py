#백트래킹과 재귀함수 사용
#https://blog.naver.com/wndud5570/222247046539

import sys
n,m =map(int, sys.stdin.readline().split())
Nlist = [1+i for i in range(n)] # 1~n 까지의 숫자 저장

visited = [False]*(n) #노드 방문 여부표시 
Result = [] #결과 값 출력하기 위한 리스트 

def dfs(depth):
    if depth == m :
        print(*Result) # 인자 값이 m일때 결과 출력 
        return
    
    for i in range(n): 
        if not visited[i] : #아직 방문하지 않은 경우 
            visited[i] = True # 방문 표시 (중복방지)
            
            Result.append(Nlist[i])
            #print(Result)
            dfs(depth+1)

            #print(Result)
            Result.pop() #뒤에 숫자 빼고 다른숫자 ex) 4C3 1 2 3 -> 1 2 -> 1 2 4 
            visited[i] = False  #방문표시 초기화
        
dfs(0)           
    
    
