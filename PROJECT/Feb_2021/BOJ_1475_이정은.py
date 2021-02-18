import math
#https://hongku.tistory.com/371 참고

n=input() 
num_space = [float(0) for i in range(10)] #0.0~ 9.0 까지의 수 저장할 리스트 생성
N = list(n) #ex, 2239 -> '2','2','3','9'

for i in range(len(n)): #n크기만큼 돌면서
    if N[i] == '6' or N[i] == '9':
        num_space[6] += 0.5 #6과 9 같은걸로 취급 후 0.5로 계산 
    else:
        num_space[int(N[i])] +=1 #그 숫자의 count ++
        #숫자마다 자릿수 찾아가서 1 or 0.5 더하기

print(math.ceil(max(num_space))) #count 최댓값 출력 
