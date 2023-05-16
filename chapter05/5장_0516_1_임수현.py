sum = 0
# 10번 반복 
for count in range (1,11,1) :
# 정수 입력할때마다 
    num = int(input(str(count) + "번째 정수를 입력하세요 :"))
# 짝수번째 숫자는 X -1
    if count % 2 == 0 :
        num *= -1
# 합계 더하기
    sum += num
# 총합 출력
print("합:{}".format(sum))