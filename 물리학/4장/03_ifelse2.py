'''
    작성일 : 2023년 9월 20일
    작성자 : 컴퓨터공학부 23학번 임수현
    설명 : 선택문 if~else
        정수를 입력받아 짝수인지 홀수인지 판단.
        짝수, 홀수는 양수일 경우만 판단.

        짝수 = 2로 나눈 나머지가 0이다.  %, ==
        홀수 = 2로 나눈 나머지가 1이다. (0이 아니다.) !=
'''

# 1.정수를 입력받는다.
num = int(input("정수 입력:"))
# 2. 판단. -판단의 기준은? 
if num > 0:
    if num % 2 == 0 :
        print(num,"은,는 짝수입니다.")
    else:
        print(num,"은,는 홀수입니다.")