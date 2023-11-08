'''
    작성일 : 2023년 11월 8일
    작성자 : 컴퓨터공학부 23학번 임수현
    설명 : 심화문제 8-6
'''
# 학생 리스트
st_tuple = [('211101', '강이안', '010-123-1111'), ('211102', '박동민', '010-123-2222'), ('211103', '김수정', '010-123-3333')]

# 학번과 이름을 딕셔너리로 만듭니다.
st_dict = {}
for st_info in st_tuple:
    st_num, name, phone = st_info  
    st_dict[st_num] = (name, phone) 

# 딕셔너리를 출력합니다.
for st_num, (name, _) in st_dict.items():
    print(f"{st_num} : {name}")

# 학번을 입력받아 학생 정보 출력
while True:
    input_number = input("학번을 입력하세요: ")
    if input_number in st_dict:
        name, phone = st_dict[input_number]
        print(f"{input_number} 학생은 {name}이며, 전화번호는 {phone}입니다.")
        break
    else:
        print("다시 입력.")
