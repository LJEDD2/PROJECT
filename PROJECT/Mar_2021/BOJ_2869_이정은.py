import sys
A,B,V = map(int, sys.stdin.readline().split())
count = 0

#while 시간초과뜸 -> 식 미리 입력받아서 한번에 처리

#낮에 정상에 도착
#밤에 떨어짐 -> 하루 이동거리 A-B 

#오르는 기간 = (V-B)/(A-B)
# 밤에 오르는 거리 제외하고 나누기


day = (V-B)/(A-B)
if day == int(day):
    print(int(day))
else:
    print(int(day)+1)
   

