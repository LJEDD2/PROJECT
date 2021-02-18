#KMP

name=str(input())
#문자열 입력받음 
split_name = name.split('-') # split()으로 구분자 구분해서 저장

initial = [] 
for i in range(len(split_name)):
    initial.append(split_name[i][0]) #이중 리스트로 인식되어 첫 번째
                                        #자릿수만 이니셜에 저장 

print("".join(initial)) # join()을 쓰면 리스트 요소 붙여서 print 가능 


#함수참고
#https://kin.naver.com/qna/detail.nhn?d1id=1&dirId=10402&docId=379249552&qb=7YyM7J207I2sIOumrOyKpO2KuCDrrLjsnpDstpzroKU=&enc=utf8&section=kin.ext&rank=1&search_sort=0&spq=0
