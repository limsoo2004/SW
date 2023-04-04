#5과목의 점수 입력받고 총합과 평균 출력하기

kor = int(input('국어 : '))
mat = int(input('수학 : '))
sci = int(input('과학 : '))
soc = int(input('사회 : '))
eng = int(input('영어 : '))

#총합 구하기

total = kor + mat + sci + soc + eng
print('점수 총합은',total,'점 입니다.')

avg = total / 5
print('평균값은 {:.2f}입니다.'.format(avg))