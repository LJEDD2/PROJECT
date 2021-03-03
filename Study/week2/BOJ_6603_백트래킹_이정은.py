import sys

#백트래킹
def Lotto(num, depth):
    if depth == 6:
        for i in range(6):
            print(combi[i], end=' ')
        print()
        return
    
    for i in range(num, len(lotto)):
        combi[depth] = lotto[i]
        Lotto(i+1, depth+1)
        
combi = [0 for _ in range(13)]
# k개 (6 < k < 13) 중 6개니까 미리 조합 저장소 생성  

while True:
    n_list = list(map(int, sys.stdin.readline().split()))

    Zero = int(n_list[0])
    if Zero == 0:
        break
    
    lotto = n_list[1:]
    
    Lotto(0,0)
    print()

