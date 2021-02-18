#일곱난쟁이
# 9개 합에서 2개의 숫자를 빼면서 100을 맞추는 방법 선택
# 나머지는 7개 추출 후 계산하여 100이 되는 수 출력
# https://blog.naver.com/k1mjunooo/222170254178 참고
A=[]
for i in range(9):
    A.append(int(input()))

A.sort() 
Sum = sum(A) # 전체 합계 
      
for i in range(8): # 0~7
    for j in range(i+1,9): #1~8 겹치지않게 모든 수 비교  
        if Sum - A[i] - A[j] == 100: #합이 100일경우 
            for k in range(len(A)):
                if k == i or k == j:
                    continue
                else:
                    print(A[k]) #A[i],A[j] 빼고 모두 출력 
            exit() #break
