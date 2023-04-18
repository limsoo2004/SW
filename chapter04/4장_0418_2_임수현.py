'''
작성일 : 2023년 4월 18일
학과 : 컴퓨터공학부
학번 : 202395026
이름 : 임수현
설명 : 입력받은 달의 계절이 무엇인지 구별하는 프로그램.
'''

# 정수 입력받음
mon = int(input("몇월달인지 입력하시오.:"))

    
# 3,4,5월은 봄
if mon >= 3 and mon <= 5:
    print("봄")
    
# 6,7,8월은 여름
elif mon >= 6 and mon <= 8:
    print("여름")

# 9,10,11월은 가을
elif mon >= 9 and mon <= 11:
    print("가을")

# 12,1,2월은 겨울
if mon == 12 or mon == 1 or mon == 2:
    print("겨울")

# 잘못된 정수를 입력한 경우
if mon <= 1 and mon >= 12:
    print("잘못된 수입니다.")