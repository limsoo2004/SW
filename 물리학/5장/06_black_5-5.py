'''
    작성일 : 2023년 9월 27일
    작성자 : 컴퓨터공학부 23학번 임수현
    설명 : 반복문으로 팩토리얼 구하기.


'''
n = int(input("정수 입력 : "))

for i in range(1,n + 1):
    f = f * i
    print(n,"!은",f,"이다.")