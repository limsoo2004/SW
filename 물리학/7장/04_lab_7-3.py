'''
    작성일 : 2023년 10월 18일
    작성자 : 컴퓨터공학부 23학번 임수현
    설명 : 도시의 인구 자료에 대한 슬라이싱을 해보자
'''
pop = ["sel",9765,"pus",3441,"icn",2954]
print("서울 인구 : ",pop[1]) 
print("인천 인구 : ",pop[-1]) #문제 2

cities = pop[0::2]
print('도시 리스트:',cities) #문제 3
pops = pop[1:2] #문제 4
print('인구의 합:', sum(pops))  