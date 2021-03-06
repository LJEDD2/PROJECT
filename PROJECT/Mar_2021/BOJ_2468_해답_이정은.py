import sys
sys.setrecursionlimit(10**6) #재귀함수의 깊이를 최대한 늘려준다.
#https://algoshipda.blogspot.com/2015/05/syssetrecursionlimit-limit.html

N = int(sys.stdin.readline())
h_graph = [list(map(int,sys.stdin.readline().split())) for i in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1] #좌우하상 좌표 


#1부터 그래프 내 최대 높이 숫자까지 돌면서 영역의 최대 개수를 count
# 물의 높이를 점점 높여가면서 탐색
#https://blog.naver.com/hoijae0194/222119752865

def dfs(x,y,h):
    visited[x][y] = True #방문했다
    for i in range(4): #동서남북으로 탐색 
        nx, ny = x+dx[i], y+dy[i] #위아래양옆으로 1만큼 이동해서 좌표 저장 
        if 0 <= nx < N and 0 <= ny < N:
            if not visited[nx][ny] and h_graph[nx][ny] > h:
                #방문x고 높이보다 크면 
                dfs(nx, ny, h) #더 깊게 탐색 , h보다 작으면 탈출하겠지? 



ans = 1
for h in range(0,101): #높이는 1이상 100 이하의 정수
    visited = [[False]*N for _ in range(N)] #방문여부 표시 
    count = 0 #카운트 

    for i in range(N): 
        for j in range(N): #그래프 (0,0)부터 탐색 
            if h_graph[i][j] > h and not visited[i][j]: #h보다 높고 방문x일경우
                count += 1 #영역 카운트 
                visited[i][j] = True #방문했다 표시
                dfs(i,j,h) # 다른 영역 있는지 탐색
                
    ans = max(ans, count) #최댓값비교

print(ans)


    

    
