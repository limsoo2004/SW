'''
작성일 : 2023년 5월 3일
학과 : 컴퓨터공학부
학번 : 202395026
이름 : 임수현
설명 : 구구단 출력

[문제 분석]
사용자가 입력한 수 : 
빼는 수:i


'''
# 1. 정수를 입력받는다.
# 2. 입력받은 정수가 1부터
# 3. 합계는 0
# 4. 입력받은 정수가 10까지 반복하면서
#   a 수를 1 증가시킨다.
#   1) 만약에 수가 입력받은 수의 배수이면 :
#       1합계를 계산한다.
#       b-1 수를 1 증가시킨다.
#   c 수를 1 증가시킨다.
#   2) 아니면(배수가 아니면)
#       b-1 수를 1 증가시킨다.


'''
num = int(input("정수 입력:"))
i = 1
result = 0

for i in range(1,1001,1):
    if i % num == 0 :
        result += i
    else:
        continue
print(result)

while
'''

num = int(input("정수 입력:"))

i = 1
result = 0

while i <1001:
    if i % num == 0 :
        result += i
        i += 1
    else:
        continue
    
print(result)
