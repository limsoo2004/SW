'''
    작성일 : 2023년 11월 1일
    작성자 : 컴퓨터공학부 23학번 임수현
    설명 : 
'''
items = {"커피음료" : 7, "펜": 3, "종이컵" : 2, "우유 : ": 1,"콜라": 4,"책":5}

# 물건의 목록을 출력한다.
#print(items.keys())
print('제품 목록 :', end=' ')  
for key in items.keys() :
    print(key, end=', ')    
print()

# 물건의 이름을 입력 받아 재고를 출력한다.
name = input("물건의 이름을 입력하시오: ")
print('재고 :', items[name])