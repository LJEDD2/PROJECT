n = int(input())
Fibo = [0,1]+[0]*(n-1) # 맨 앞 0,1 놔두고 총 n+1개의 칸이 되도록 배열 할당

for i in range(2,n+1): # 3번째자리부터 ~ 마지막까지 
    Fibo[i] = Fibo[i-1]+Fibo[i-2] #피보나치 공식 
    #print(Fibo)
print(Fibo[n]) #n번째 피보나치 수 출력
