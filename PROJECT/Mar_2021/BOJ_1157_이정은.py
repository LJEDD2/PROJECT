n =input().upper()
#https://blog.naver.com/taker829/222229212017
n_list= list(set(n)) # set()을 통해 중복문자를 제거 후 비교할 문자 선별
#num_space - > ['E', '_', 'N', 'C', 'S', 'M', 'A', 'U', 'P']
#aassdaaa -> ['D', 'A', 'S']

n_count = []

for i in n_list :
    count = n.count(i)
    n_count.append(count)


'''for i in range(len(n)):
    if n[i].isalpha() == True:
        num_space.append(ord(n[i]))
        이걸 쓸필요가 없다 ㅠ 시간 잡아먹는 범인
'''
if n_count.count(max(n_count)) > 1: #가장 큰 cnt가 1개만 있는 것이 아닐 경우
    # n_cnt.count(count()) 사용한것  
    print("?")
else:
    maxv = n_count.index(max(n_count)) #맥스값 저장
    print(n_list[maxv]) #맥스값 인덱스 값 출력 
