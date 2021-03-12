import sys
from collections import deque
#https://blog.naver.com/repeater1384/222251161279

n = int(sys.stdin.readline())
graph = [[*map(int, sys.stdin.readline().split())] for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

#과정
#0이 아닌 물고기의 좌표 저장
#내림차순 소팅하면서 동점은 걸리는 시간 내림차순 sort
            
def find_near_fish(_matrix, _sx, _sy, _size): #_sx,_sy는 현재 상어의 위치
    fishes = []
    visited = [[False] * n  for _ in range(n)]
    queue = deque([(0, _sy, _sx)])
    visited[_sy][_sx] = True
    
    while queue:
        print(queue)
        distance, cy, cx = queue.popleft()
        
        for i in range(4):
            nx, ny = cx + dx[i] , cy + dy[i]
            #갈 수 있는 칸
            if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx]:
                
                if 0 <= _matrix[ny][nx] <= _size:
                    queue.append((distance + 1, ny, nx ))
                    visited[ny][nx] = True

                    #상어가 먹을수 있는 물고기 
                    if 0 < _matrix[ny][nx] < _size:
                        fishes.append([distance + 1, ny, nx])

    fishes.sort() #물고기까지의 거리 소팅

    if fishes:
        return fishes[0] #비어있으면 None

# 상어를 찾아서 0으로 표시하고 위치를 저장
for y in range(n):
    for x in range(n):
        if graph[y][x] == 9: #2차원배열이라 x와 y자리 뒤바껴있음 주의
            shark_x, shark_y=  x,y
            graph[y][x] = 0
            break
ans = 0
shark = 2
eat_count = 0

while True:
    result = find_near_fish(graph, shark_x, shark_y, shark)

    if result is None:
        #먹을 수 있는 물고기가 없을 경우 answer출력
        print(ans)
        break

    fish_distance, fish_y, fish_x = result
    graph[fish_y][fish_x] = 0

    #먹은 물고기 수, 소요된 시간 카운트
    eat_count += 1
    ans += fish_distance

    #물고기 위치로 이동 
    shark_y , shark_x = fish_y , fish_x

    #크기 레벨업
    if shark == eat_count :
        shark += 1
        eat_count = 0 #카운트 초기화 
    
            
            
            
        
