from itertools import combinations
import sys

N,M = map(int,input().split())
city = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
c,h = [], []
result = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            h.append([i,j])
        if city[i][j] == 2:
            c.append([i,j])


#1. 살려야할 집
            # 치킨집 배열 중에서 각 집과의 합이 제일 작은 수를 기준으로
            # 각 집의 최소 치킨거리 / 치킨집 기준으로 도시치킨거리 구한다.
#2. 치킨거리
