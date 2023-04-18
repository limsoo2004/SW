'''
작성일 : 2023년 4월 18일
학과 : 컴퓨터공학부
학번 : 202395026
이름 : 임수현
설명 : 입력받은 점수의 학점이 무엇인지 구별하는 프로그램.
'''

# 점수 입력받음
score = int(input("점수를 입력하시오 :"))

# 점수는 0 ~ 100을 넘을 수 없음
score <= 100 and score >=0
# 만약 잘못된 정수를 넣을 경우 "잘못된 점수입니다." 출력
if score >=100 or score <=0:
    print("잘못된 점수입니다.")

# 100 ~ 90점이면 A
if score <= 100 and score > 90:
    print("A학점")

# 89 ~ 80점이면 B
elif score <= 90 and score > 80:
    print("B학점")

# 79 ~ 70점이면 C
elif score <= 80 and score > 70:
    print("C학점")

# 69 ~ 60점이면 D
elif score <= 70 and score > 60:
    print("D학점")

# 나머지 F
elif score <= 60 and score > 0:
    print("F학점")
    
