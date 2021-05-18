import sys

n = int(sys.stdin.readline())
stack = [int(sys.stdin.readline()) for _ in range(n)]
top = stack[-1]
cnt = 1 #맨오른쪽은 무조건 포함되므로

for i in range(n-1,-1,-1):
    if stack[i] < top or stack[i] == top:
        del stack[i]

print(len(stack)+1)

       
