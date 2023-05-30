'''
작성일 : 2023년 5월 30일
학과 : 컴퓨터공학부
학번 : 202395026
이름 : 임수현
설명 : 8장 파일 입출력 
'''

# open() 함수로 파일 쓰기 - write() 메소드
f = open("test.txt","w")
for i in range(1,11) :
    f.write("{}번째 메세지입니다. \n" .format(i))
    f.close()   #파일 종료