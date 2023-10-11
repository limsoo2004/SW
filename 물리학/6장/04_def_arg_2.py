'''
    작성일 : 2023년 10월 11일
    작성자 : 컴퓨터공학부 23학번 임수현
    설명 : 여러 개의 값을 넘겨주고 여러개의 값을 돌려받기.

    두 수를 전달하여 사칙 연산의 결과값을 돌려주는 함수.

    [알고리즘]
    (함수)
        3. 전달받은 2개의 값을 매개 변수에 저장.
        4. 두 수를 가지고 사칙연산을 계산한다.
        5. 사칙연산의 결과 5개를 돌려준다.
    (메인)
        1. 두 수를 입력받는다.
        2. 두 수를 가지고 함수를 호출한다.
        6. 돌려받은 결과를 출력한다.
'''
# 함수 선언
def cals(n1, n2) :
    sum = n1 + n2
    minus = n1 - n2
    mul = n1 * n2
    div = n1 / n2
    rest = n1 & n2
    return sum, minus, mul, div, rest #돌려주는 결과는 5개

n1 = int(input("첫번쨰 수 입력 : "))
n2 = int(input("두번쨰 수 입력 : "))

sum, minus,mul,div,rest = cals(n1,n2)
print(f"{n1} + {n2} = {sum}")
print(f"{n1} - {n2} = {minus}")
print(f"{n1} * {n2} = {mul}")
print(f"{n1} / {n2} = {div}")
print(f"{n1} & {n2} = {rest}")