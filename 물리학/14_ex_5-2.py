'''
    작성일 : 2023년 10월 4일
    작성자 : 컴퓨터공학부 23학번 임수현
    설명 : 1. 두 수를 입력받아
        2. 두 수 사이의 합계 출력
        3.두 수 사이의 짝수의 합계 출력

        심화문제 5-2, 141페이지
        for 또는 while 중 원하는 것 사용.
'''

# 두 수 입력받음
n1 = int(input("첫 번째 수를 입력하세요: "))
n2 = int(input("두 번째 수를 입력하세요: "))

# 두 수 합계 계산

if n1 < n2 :
    sum1 = 0

    for num in range(n1, n2 + 1):
        sum1 += num

    # 두 수의 짝수의 합계 계산
    sum2 = 0
    for num in range(n1, n2 + 1):
        if num % 2 == 0:
            sum2 += num

    # 결과 출력
    print(f"{n1}부터 {n2}까지의 합계: {sum1}")
    print(f"{n1}부터 {n2}까지의 짝수의 합계: {sum2}")
elif n1 > n2 :
    sum1 = n1 + n2

    for num in range(n2, n1 + 1):
        sum1 += num

    # 두 수의 짝수의 합계 계산
    sum2 = 0
    for num in range(n2, n1 + 1):
        if num % 2 == 0:
            sum2 += num

    # 결과 출력
    print(f"{n2}부터 {n1}까지의 합계: {sum1}")
    print(f"{n2}부터 {n1}까지의 짝수의 합계: {sum2}")