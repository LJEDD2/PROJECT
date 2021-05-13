'''
n = int(input())
s_list=[]
for i in range(n):
    s_list.append(list(map(str,input().split())))


for i in range(n):
    for j in range(len(s_list[i])):
        print(s_list[i][j][::-1],end=" ")
        
    print("")
'''

from collections import deque # stack 라이브러리
import sys
T = int(sys.stdin.readline())
dq = deque() # 스택 생성
for _ in range(T):
    lst = []
    N = sys.stdin.readline()# 문자열 입력
    for idx, i in enumerate(N):
        if i == " ": # 공백이 나오면 스택에 있는 문자 출력
            for j in range(len(dq)):
                lst.append(dq.pop())
            lst.append(' ')
        elif idx == len(N)-1:
            for j in range(len(dq)):
                lst.append(dq.pop())
            lst.append(i)
        else:
            dq.append(i)
    sys.stdout.write(''.join(lst))
