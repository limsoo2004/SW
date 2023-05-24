'''
실습 예제 7-1
랜덤으로 1~100 사이의 값을 10개 생성한 세트 2개 만들고,
합집합, 교집합, 차집합을 출력하시오.
[알고리즘]
1. 비어있는 세트 2개 만들기
2. 랜덤으로 2개의 세트에 각각 10개의 값 저장
    반복하면서 10개의 
    1) 값 저장(추가)
3. 2개의 세트 값 출력
    합집합,교집합,차집합 출력
'''

# print("set1과 set2의 합집합", set1 | set2)
# print("set1과 set2의 교집합", set1 & set2)
# print("set1과 set2의 차집합", set1 - set2)

import random

num1 = set()    #set()함수로 비어있는 세트 생성
num2 = set()

for i in range(10) :
    num1.add(random.randint(1,10))
    num2.add(random.randint(1,10))

print("num1과 num2의 합집합", num1 | num2)
print("num1과 num2의 교집합", num1 & num2)
print("num1과 num2의 차집합", num1 - num2)
