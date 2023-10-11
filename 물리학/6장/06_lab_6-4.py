'''
    작성일 : 2023년 10월 11일
    작성자 : 컴퓨터공학부 23학번 임수현
    설명 : LAB 6-4 리스트에서 최대값, 최소값을 찾아 돌려주는 함수.

    리스트에 10개의 값을 랜덤으로 생성하고,
    max, min을 입력받아 최대, 최소값을 찾아 돌려주는 함수.

    (함수)
        5) 두 값을 전달받아 배개 변수에 저장.
        6) 최대값 최소값을 찾는다.
        7) 돌려준다.
    (메인)
        1.무한반복
            1) 랜덤으로 10에서 99까지 10개의 수를 리스트로 생성
            2) 생성된 리스트를 출력
            3) 사용자로부터 최대값을 알고 싶은지 최소값을 알고 싶은지 묻는다.
                사용자가 입력할 값은 max 또는 min
            4) 입력받은 max 또는 min과 생성된 리스트를 가지고 함수 호출
            8)돌려받은 최대값 또는 최소값을 출력한다.
'''
import random

# 최대값을 찾는 함수
def find_max(nums):
    max_value = max(nums)
    return max_value

# 최소값을 찾는 함수
def find_min(nums):
    min_value = min(nums)
    return min_value

while True:
    # 10개의 랜덤 숫자 생성
    random_numbers = [random.randint(10, 99) for _ in range(10)]

    # 생성된 리스트 출력
    print("생성된 리스트:", random_numbers)

    # 사용자로부터 최대값 또는 최소값 입력 받기
    choice = input("최대값은 'max', 최소값은 'min'을 (종료하려면 'q' 입력): ")

    # q로 탈출
    if choice == 'q':
        break
    # max 입력시 최대값 출력
    elif choice == 'max':
        max_value = find_max(random_numbers)
        print("최대값:", max_value)
    # min 입력시 최소값 출력
    elif choice == 'min':
        min_value = find_min(random_numbers)
        print("최소값:", min_value)
    # 다른 걸 입력시 오류 메시지 출력
    else:
        print("'max', 'min', 또는 'q' 중 하나를 입력.")
