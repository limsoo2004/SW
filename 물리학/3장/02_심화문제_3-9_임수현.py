'''
    작성일 : 2023년 9월 13일
    작성자 : 컴퓨터공학부 23학번 임수현
    설명 : 90페이지 문제 3.9 
          평균 시속과 이동시간을 입력받아 
          이동 시간은 시,분,초 단위로 출력하고, 
          이동한 거리를 계산하여 출력하시오.
'''

avsp = float(input("평균 시속을 입력하세요 (km/h): "))
tt = float(input("이동 시간을 입력하세요 (h): "))
print("평균 시속:",avsp,"km/h")

h = int(tt)
lm = (tt - h) * 60
m = int(lm)
ls = (lm - m) * 60
s = round(ls)
print("이동 시간:{}시간 {}분 {}초".format(h,m,s))
print("이동 거리: {}km".format(tt*avsp))