import sys


M,N = map(int,sys.stdin.readline().split()) # 가로 세로 입력
board = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

#도형 총 19개 일일히 다 비교하는 코드
#https://blog.naver.com/acdy123/222058848314
#https://myjamong.tistory.com/141
#https://blog.naver.com/kswamen/222163247781

def calc(i,j): #i는 세로 j는 가로
    global sum_max

    # line형 조각
    if j + 3 < N: # 가로로 4만큼 뻗칠 수 있는 경우 
        sumv = board[i][j]+board[i][j+1]+board[i][j+2]+board[i][j+3]
        sum_max = max(sumv, sum_max)
    if i + 3 < M: #세로로 4만큼 뻗칠 수 있는 경우 
        sumv = board[i][j]+board[i+1][j]+board[i+2][j]+board[i+3][j]
        sum_max =max(sumv, sum_max)
    #box형 조각
    if  i+1 < M and j+1 < N: # 가로 세로 2칸만큼 뻗칠 수 있는 경우
        sumv = board[i][j]+board[i+1][j]+board[i+1][j+1]+board[i][j]
        sum_max = max(sumv, sum_max)
    #가로 3 세로 2인 경우의 도형 
    if j+2 < N and i+1 <M : #가로 3 세로 2칸만큼 뻗칠 수 있는 경우 
        sumv1 = board[i][j]+board[i][j+1]+board[i][j+2]+board[i+1][j+2]
        sumv2 = board[i][j]+board[i][j+1]+board[i][j+2]+board[i+1][j+1]
        sumv3 = board[i][j]+board[i][j+1]+board[i+1][j+1]+board[i+1][j+2]
        sumv4 = board[i][j]+board[i+1][j]+board[i+1][j+1]+board[i+1][j+2]
        sumv5 = board[i][j]+board[i+1][j]+board[i][j+1]+board[i][j+2]
        sum_max = max(sum_max , sumv1, sumv2, sumv3, sumv4, sumv5)
    #세로 3 가로 2인 경우의 도형 
    if i+2 < M and j+1 <N :
        sumv1 = board[i][j]+board[i+1][j]+board[i+2][j]+board[i+1][j+1]
        sumv2 = board[i][j]+board[i+1][j]+board[i+2][j]+board[i+2][j+1]
        sumv3 = board[i][j]+board[i][j+1]+board[i+1][j+1]+board[i+2][j+1]
        sumv4 = board[i][j]+board[i+1][j]+board[i+1][j+1]+board[i+2][j+1]
        sumv5 = board[i][j]+board[i+1][j]+board[i+2][j]+board[i][j+1]
        sum_max = max(sum_max , sumv1, sumv2, sumv3, sumv4, sumv5)
    # 세로 3 가로 -2인 경우의 도형 (대칭한 경우) 
    if i+2 < M and j-1 >= 0:
        sumv1 = board[i][j]+board[i+1][j]+board[i+2][j]+board[i+1][j-1] 
        sumv2 = board[i][j]+board[i+1][j]+board[i+2][j]+board[i+2][j-1]  
        sumv3 = board[i][j]+board[i+1][j]+board[i+1][j-1]+board[i+2][j-1] 
        sum_max = max(sum_max ,sumv1, sumv2, sumv3)
    # 세로 2 가로 -3 인 경우의 도형 (대칭한 경우 2)
    if i+ 1< M and j-2 >= 0 : # 왼쪽으로 3칸뻗으면서 0이 되지않도록 
        sumv = board[i][j]+board[i+1][j]+board[i+1][j-1]+board[i+1][j-2] 
        sum_max = max(sum_max , sumv)
    # 세로 2 가로 -2 인 경우의 도형 (대칭한 경우 3)
    if i+1 < M and j-1 >= 0 and j+1< N : # 세로로 2칸 가로 왼쪽으로 2칸뻗음 (음수x) 
        sumv = board[i][j]+board[i+1][j]+board[i+1][j-1]+board[i+1][j+1]
        sumv1 = board[i][j]+board[i+1][j]+board[i+1][j-1]+board[i][j+1]
        sum_max = max(sum_max,sumv,sumv1)

sum_max = 0
for i in range(M):
    for j in range(N):
        calc(i,j)


print(sum_max)

        
