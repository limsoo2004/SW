'''
    작성일 : 2023년 11월 8일
    작성자 : 컴퓨터공학부 23학번 임수현
    설명 : 집합 set()
'''

# 비교 연산자
num1 = {1,2,3}
num2 = {1,2,3}
print("num1 == num2 ? ",num1 == num2)

# 6개의 숫자로 집합 생성
num_set = {1,4,6,3,7,4}
print("num_set : ", num_set)
print("num_set 길이 : ",len(num_set))
print("num_set 중 가장 큰 값",max(num_set))
print("num_set 중 가장 작은 값",min(num_set))
print("num_set 합계",(num_set))

num1 = {1,2,3}
num2 = {3,4,5}

# 합집합
print('num1 | union(num2) :',num1.union(num2)) #합잡헙 메소드 union()
