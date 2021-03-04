N , money= map(int,input().split())
Won = []
minv = 0

for i in range(N):
    Won.append(int(input()))

#그리디알고리즘을 통해 문제를 해결해야한다
#큰수 순서대로 개수를 구해야함 -> 최소 개수가 문제
#https://blog.naver.com/sce06179/222248411933
    
Won.sort(reverse=True)

for i in range(len(Won)):
    if money == 0:
        break
    minv += money // Won[i] #몫을 최소값에 저장 
    money %= Won[i] # 나머지
    #ex ) 4200보다 Won[i]값이 크면 몫 0 나머지 4200이 된다.
    

print(minv)   
    




    
        
