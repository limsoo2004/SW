'''
    작성일 : 2023년 9월 20일
    작성자 : 컴퓨터공학부 23학번 임수현
    설명 : random을 이용한 가위바위보 게임.

    random 함수로 생성된 정수를 가지고 게임을 진행합니다.
    0 = 가위 1 = 바위 2 = 보

    두 명의 플레이어의 이름을 입력받아 가위바위보 게임을 진행합니다.
'''
import random #random 함수 가져오기.(포함시키기)

print(":: 가위바위보 게임 시작 ::")

player1 = input

num1 = random.randrange(3) #랜덤으로 012 생성하여 변수에 저장.
num2 = random.randrange(3) #랜덤으로 012 생성하여 변수에 저장.
#p1의 가위 바위 보 출력 
if num1 == 0 :
    print(player1,":",end = '')
    print('가위')
if num1 == 1 :
    print('바위')
if num1 == 2 :
    print('보')

player2 = input

random.randrange(3)
#p2의 가위 바위 보 출력 
if num2 == 0 :
    print(player2,":",end = '')
    print('가위')
elif num2 == 1 :
    print('바위')
else :
    print('보')

if num1 == '바위' and num2 =='가위' :
    print("p1 승리")
    if num1 == '가위' and num2 =='보' :
        print("p1 승리")
    if num1 == '보' and num2 =='바위' :
        print("p1 승리")

elif num1 == num2:
    print("draw")
else : 
    print("p2 승리")    
