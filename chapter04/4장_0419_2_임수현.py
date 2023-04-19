'''
작성일 : 2023년 4월 19일
학과 : 컴퓨터공학부
학번 : 202395026
이름 : 임수현
설명 : 연산자를 구별하는 프로그램.
'''

# 숫자와 연산자 입력받음.
num1 = int(input("첫번째 수:"))
num2 = int(input("두번째 수:"))
cal = input("연산자:")

if cal == "+" :
    print("{} + {} = {}" .format(num1,num2,num1+num2))
elif cal == "-" :
    print("{} - {} = {}" .format(num1,num2,num1-num2))  
elif cal == "*" :
    print("{} * {} = {}" .format(num1,num2,num1*num2))  
elif cal == "/" :
    print("{} / {} = {}" .format(num1,num2,num1/num2))  
else :
    print("연산자 없음")
    