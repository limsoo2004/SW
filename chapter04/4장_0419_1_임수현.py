'''
작성일 : 2023년 4월 19일
학과 : 컴퓨터공학부
학번 : 202395026
이름 : 임수현
설명 : 탑승 가능한 롤러코스터가 무엇인지 구별하는 프로그램.
'''

# 나이와 키를 입력받는다.
age = int(input("나이:"))
heig = int(input("키:"))

# 나이가 8살을 넘을 때 
if age >= 8:
    # 키가 120cm이상이면 고속 롤러코스터 탑승 가능
    if heig >= 120 :
        print("고속 롤러코스터 탑승 가능")
    # 키가 120cm이하면 저속 롤러코스터 탑승 가능
    else :
        print("저속 롤러코스터 탑승 가능")
# 나이가 안넘으면
else:
    print("탑승 불가")
    
    
    