'''
작성일 : 2023년 4월 12일
학과 : 컴퓨터공학부
학번 : 202395026
이름 : 임수현
설명 : 입력받은 점수의 학점이 무엇인지 구별하는 프로그램.
'''
# 점수 입력받음
num = int(input("점수를 입력하시오 :"))
# 100 ~ 90점이면 A
if num <= 100 and num >= 90:
    print("A학점")
# 89 ~ 80점이면 B
elif num <= 89 and num >= 80:
    print("B학점")
# 79 ~ 70점이면 C
elif num <= 79 and num >= 70:
    print("C학점")
# 69 ~ 60점이면 D
elif num <= 69 and num >= 60:
    print("D학점")
# 나머지 F
else :
    print("F학점")
