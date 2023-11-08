'''
    작성일 : 2023년 11월 8일
    작성자 : 컴퓨터공학부 23학번 임수현
    설명 : 심화문제 8-3
    1. 학번,이름,전화번호 3쌍의 요소를 가지는 
    student_tuple이라는 튜플이 존재한다.
    2. 이 튜플을 수정하여 {학번 : [이름, 전화번호]}의 쌍으로 
    이룽어진 딕셔너리를 만들어 출력하시오.
    3.이 정보를 이용하여 학생의 학번을 입력받아 이름과 전화번호를 출력하는 학사정보 프로그램을 작성
    student_tuple1
    4. student_tuple의 마지막 항목으로 학점을 추가한다.
    이 정보를 바탕으로 딕셔너리를 만들어 출력하시오.

    5. 학생의 학점 평균을 출력하시오.
'''

student_tuple = [('202395021','임수현','010-3161-1753')('202395022','임수현','010-3161-1753')('202395023','임수현','010-3161-1753')]
student_dict = {}
# 딕셔너리에 추가
for id_num, name, phone in student_tuple :
    student_dict[id_num] = [name, phone]

# 딕셔너리 내용 출력
for key, value in student_dict :
    print(key, ":",value)

# 학번 입력받아 이름과 연락처 출력
number = input("학번을 입력하시오 : ")
print('이름 : ', student_dict[number])
print('연락처 : ',student_dict[number][1])

# 4. student_tuple의 마지막 항목으로 학점을 추가한다.
student_dict['202395021'].append[4.1]
student_dict['202395022'].append[4.2]
student_dict['202395023'].append[4.3]

for key, value in student_dict.items() :
    print(key," : ", value)

# 5. 학생의 학점 평균을 출력하시오.
print("전체 학생 평균 학점")
for key, value in student_dict.items() :
    sum = sum + value[2]

print(f"평균 : {(sum/3):.2f}")