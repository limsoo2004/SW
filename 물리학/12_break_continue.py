'''
    작성일 : 2023년 10월 4일
    작성자 : 컴퓨터공학부 23학번 임수현
    설명 : 반복을 제어하는 break, continue 
        교재 137페이지

    Test word : programming
'''

# 단어 입력
word = input("단어를 입력하세요  :")

print(":: break1 ::")
# 문자 개수만큼 반복
for i in word :
    # 만약 i가 모음이라면
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' :
        # 반복 종료
        break 
    # 아니라면 i 출력하고 종료
    else :
        print(i,end='')

print(":: break2 ::")

for i in word :
    # 만약 i가 모음이라면
    if i in ['a','e','i','o','u','A','E','I','O','U'] :
        # 반복 종료
        break 
    # 아니라면 i 출력하고 종료
    else :
        print(i,end='')

print(":: continue ::")

for i in word :
    if i in ['a','e','i','o','u','A','E','I','O','U'] :
        continue    # 반복의 처음으로 돌아간다. 아래 문장를 만날 수 없다.
    print(i,end='')