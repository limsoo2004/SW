# 무한반복
while 1:
    print("=================================")
    mon = int(input("가장 좋아하는 월은?"))
        # 잘못된 정수를 입력한 경우
    if mon < 1 and mon >= 12:
        print("잘못된 수입니다.")
        continue
    print("=================================")
    if mon == 0:
        break
    print("******",mon,"월 ******")
    # 3,4,5월은 봄
    if mon >= 3 and mon <= 5:
        print(mon,"월은 봄에 해당됩니다.")
        
    # 6,7,8월은 여름
    elif mon >= 6 and mon <= 8:
        print(mon,"월은 여름에 해당됩니다.")

    # 9,10,11월은 가을
    elif mon >= 9 and mon <= 11:
        print(mon,"월은 가을에 해당됩니다.")

    # 12,1,2월은 겨울
    else:
        print(mon,"월은 겨울에 해당됩니다.")
