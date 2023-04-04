#윗변, 아랫변, 높이 입력받기

top = int(input('윗변 :'))

bottom = int(input('아랫변 :'))

height = int(input('높이 :'))

# 윗변과 아랫변 더하기
tmp1 = bottom + top
# 윗변+아랫변에 높이 곱하기
tmp2 = tmp1 * height
# 윗변+아랫변X높이 값을 2로 나누기
width = tmp2 / 2

print('윗변 값은 {}, 아랫변 값은 {}, 높이는 {}입니다.'.format(top,bottom,height))
print('넓이는 {} 입니다.'.format(width))