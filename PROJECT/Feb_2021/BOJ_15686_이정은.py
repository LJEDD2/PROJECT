from itertools import combinations
import sys

#좌표 저장 
N,M = map(int,input().split())
city = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
c,h = [],[]

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            h.append([i,j])
        if city[i][j] == 2:
            c.append([i,j])


#좌표 구하는 함수 https://blog.naver.com/kswamen/222165983276 참고
c_combi = combinations(c,M)

def dist(h_x, h_y, c):
    dist = int(1e9) #10의 9승 설정 -> 최소인지 비교하면서 줄여나가는 방법 
    for c_x , c_y in c : #c의 x,y값 
        dist = min(dist, abs(c_x-h_x)+abs(c_y-h_y))
        #print(dist)
    return dist #각 집의 치킨거리의 최솟값 리턴 

s=int(1e9) 

for ch in c_combi: #뽑은 M개의 치킨집에서  
    temp = 0
    for h_x,h_y in h: # 홈좌표 별로 
        temp += dist(h_x, h_y, ch) #각 치킨집과의 치킨거리 최솟값을 구하고 저장
    s = min(s,temp) #s에 최솟값 저장 
print(s)


