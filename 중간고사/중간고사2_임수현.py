'''
학과 : 컴퓨터공학부
학번 : 202395026
이름 : 임수현
설명 : 일반 온도와 습구 온도를 입력받아 불쾌지수를 소수점 이하 2자리까지 출력하는 프로그램이다.
소수점 둘째 자리까지 출력해야 하므로 format과 :.2f를 사용한다.

알고리즘 :
일반 온도와 습구 온도를 입력받는다.
주어진 식에 입력받은 일반 온도와 습구 온도를 대입한다.

'''
# 일반 온도와 습구 온도를 입력받음.
nortemp = float(input("일반 온도 :"))
humtemp = float(input("습구 온도 :"))
# "40.6 + 0.72 * (일반 온도 + 습구 온도)"에 대입한다.
badsco = 40.6 + 0.72 * (nortemp + humtemp)
# 불쾌지수를 소수 둘째 자리까지 출력한다.
print("불쾌지수는{:.2f}점입니다.".format(badsco))