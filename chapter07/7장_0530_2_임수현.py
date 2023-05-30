'''
작성일 : 2023년 5월 30일
학과 : 컴퓨터공학부
학번 : 202395026
이름 : 임수현
설명 : 7장 세트와 딕셔너리 
        02.딕셔너리

예제 7-3
5명의 학번과 이름을 입력하여 딕셔너리에 저장한다.
키 : 학번   값 : 이름
학번을 입력받아 해당 학생의 이름을 출력한다.
입력 받은 학번이 없으면 "입력한 학생이 존재하지 않습니다." 출력한다.
학번을 입력할 때 사용자가 0을 입력하면 프로그램을 종료한다.
'''

# 알고리즘
# 1.빈 딕셔너리 선언. - 학생 딕셔너리 만든다.
# 2.5번 반복하면서
#   1)학번을 입력받는다. 
#   2)이름을 입력받는다.
# 3.저장된 학생 정보를 출력한다.
# 4.0이 입력될때까지 반복한다.  (무한반복하면서)
#   1)검색할 학번을 입력받는다.
#   2)만약에 학번이 0이면
#       1 프로그램 종료
#   2)아니면
#       1 학생 정보 출력

student = {}
for i in range(5) : 
    id = int(input(str(i + 1) + "번쨰 학생 학번 입력 : "))
    # name = input(str(i + 1) + "번쨰 학생 학번 입력 : ")
    student[id] = '' #해당 키에 값 저장
    
print("학생 명부 완성")
print(student)

while True :
    id = int(input("검색을 원하는 학생 학번 입력(종료:0) : "))
    if id == 0 :
        print("프로그램을 종료합니다.")
        break
    else :
        if id in student : 
            print("==검색한 학생 정보==")
            print("학번 : ", id ,"이름 : ",student.get(id))
            print("학번 : ", id ,"이름 : ",student(id))
        else : 
            print("검색한 학생이 존재하지 않습니다.")