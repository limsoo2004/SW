'''
    작성일 : 2023년 10월 11일
    작성자 : 컴퓨터공학부 23학번 임수현
    설명 : 함수에 여러 개의 값 넘겨주기

    두 수를 입력받아 함수를 호출하여 두 수 사이의 합을 계산하여 돌려주는 함수

    [알고리즘]
    (함수)
        3. 두 수를 전달받아 매개변수에 저장한다.
        4. 두 수 사이의 합을 계산한다.
        5. 계산된 합을 함수를 호출한 곳으로 돌려준다.

    (메인)
        1. 두 수를 입력받는다.
        2. 두 수를 가지고 함수를 호출한다.
        6. 돌려받은 합을 출력한다.
'''
print("두 수 사이의 합 구하기(매개변수가 2개인 함수)")
# 함수 선언
def get_sum(start, end) : #전달 받은 2개의 값을 저장할 매개 변수 2개.
    sum = 0
    for i in range(start,end+1) : #두 수 사이의 합계 계산
        sum += i
    return sum #합계를 돌려준다.

# 메인
num1 = int(input("시작 수 입력"))
num2 = int(input("종료 수 입력"))

sum = get_sum(num1,num2)
print(f"{num1}부터{num2}까지 합은 {sum}입니다.")
print(f"{num1}부터{num2}까지 합은 {get_sum(num1, num2)}입니다.")
