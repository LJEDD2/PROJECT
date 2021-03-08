#Python deque 사용 예제
#https://blog.naver.com/websearch/222126631799
''' Deque란?
double-ended queue의 줄임말, 양방향으로 자료를 처리할 수 있는 queue형 자료구조
기본 queue는 선입선출의 구조이지만 덱은 양쪽에서 삽입과 삭제가 가능하다 '''

''' DFS/BFS를 구현시 유용하게 사용가능하다 '''

from collections import deque

#선택적 인수 maxlen은 deque객체에 저장할 수 있는 최대 개수를 지정한다.

clsQueue = deque(range(10), maxlen = 10)
#deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)

#.rotate()
#양수 인수를 받으면 오른쪽 항목을 지정한 개수만큼 왼쪽으로 이동
#음수 인수를 받으면 왼쪽 항목을 지정한 개수만큼 오른쪽으로 이동

#.appendleft()
#왼쪽 끝에 입력값이 저장되고 오른쪽 끝의 값이 제거.
#maxlen이 지정되어야함

#.extend()
#오른쪽 끝에 값이 저장되고 입력된 값의 개수만큼 왼쪽 끝의 값이 제거

#.extendleft(iter)
#iter 인수에서 생성되는 항목을 오른쪽에 있는 것 부터
#덱의 왼쪽에다가 하나씩 차례로 추가

#.pop() - 오른쪽 원소 반환하면서 삭제
#.popleft() - 왼쪽 원소 반환하면서 삭제 
