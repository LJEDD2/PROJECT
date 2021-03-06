import sys
sys.setrecursionlimit(10**6) #재귀함수의 깊이를 최대한 늘려준다.

N = int(sys.stdin.readline())
h_graph = [list(map(int,sys.stdin.readline().split())) for i in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1] #좌우하상 좌표 


#1부터 그래프 내 최대 높이 숫자까지 돌면서 영역의 최대 개수를 count
# 물의 높이를 점점 높여가면서 탐색

#좌표값이 그래프 내에 포함되는지 판단 
def Is_Board(i,j):
    return 0 <= i < N and 0 <= j < N


def dfs(x,y,h):
    visited[x][y] = True
    for i in range(4): #동서남북으로 탐색
        si, sj = x + dx[i], y + dy[i]  #위아래양옆으로 1만큼 이동해서 좌표 저장
        if Is_Board(si,sj): 
            if not visited[si][sj] and h_graph[si][sj] > h :
                dfs(si,sj,h)
                
        
maxv = 1 
for h in range(100): #높이는 1이상 100 이하의 정수
    visited = [[False]*N for _ in range(N)] #수위 올라갈때마다 방문 초기화
    count = 0 #카운트 초기화

    for i in range(N):
        for j in range(N):
            if h_graph[i][j] > h and not visited[i][j]:
                count += 1
                visited[i][j] = True
                dfs(i,j,h)
                
    maxv = max(count,maxv)
    
print(maxv)
    
