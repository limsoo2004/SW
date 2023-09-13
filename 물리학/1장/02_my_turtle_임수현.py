'''
    작성일 : 2023년 9월 13일
    작성자 : 컴퓨터공학부 23학번 임수현
    설명 : 
'''
import turtle as t


# 선그리기
# t.forward(200) #200픽셀 이동

# # 삼각형 그리기
# t.forward(200)
# t.left(120)
# t.forward(200)
# t.left(120)
# t.forward(200)
# t.left(120)

# 반복문으로 삼각형 그리는 코드
for i in range(181) :
    t.forward(2)
    t.left(360/180)