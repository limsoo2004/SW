'''
작성일 : 2023년 4월 12일
학과 : 컴퓨터공학부
학번 : 202395026
이름 : 임수현
설명 : 입력받은 수가 음수인지 양수인지 0인지 구별하시오.
'''

# 숫자 입력받음
num = int(input("수를 입력하세요 :")) 

# 입력바등ㄴ 정수가 0보다 큰 수인가?
if num > 0 : 
    print(num,"은(는) 양수입니다.")
# 입력받은 정수가 0보다 작은 수인가?
elif num < 0 :
    print(num,"은(는) 음수입니다.")
# 둘다 아니라면 0
else :
    print(num,"입니다.")