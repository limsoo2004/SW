'''
작성일 : 2023년 4월 19일
학과 : 컴퓨터공학부
학번 : 202395026
이름 : 임수현
설명 : 구구단 출력

[문제 분석]
사용자가 입력한 수 : 
빼는 수:i
'''
# 수 입력받음
n = int(input("수:"))
# 결과값 초기화
result = 1
# 1부터 n까지 반복
for i in range(1, n+1):
    # 1부터 n까지 1씩 더하면서 곱셈
    result *= i
# 출력
print(result)