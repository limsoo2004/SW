'''
    작성일 : 2023년 11월 1일
    작성자 : 컴퓨터공학부 23학번 임수현
    설명 : LAB 7-6 - 도시의 이름과 인구를 튜플로 묶어 최대, 최소, 평균 인구를 계산하는 프로그램
'''

# 도시 정보를 튜플로 묶은 리스트 생성
city_info = [('서울', 9765), ('부산', 3441), ('인천', 2954), ('광주', 1501), ('대전', 1531)]

# 초기화
max_pop = city_info[0][1]  # 최대 인구 초기값 설정
min_pop = city_info[0][1]  # 최소 인구 초기값 설정
total_pop = 0  # 전체 인구 합 초기값 설정

max_city = city_info[0][0]  # 최대 인구를 가진 도시 초기값 설정
min_city = city_info[0][0]  # 최소 인구를 가진 도시 초기값 설정

# 도시 정보를 순회하면서 최대, 최소, 총 인구 계산
for city, population in city_info:
    total_pop += city[1]  # 전체 인구 합산
    if city[1] > max_pop:
        max_pop = city[1]  # 최대 인구 갱신
        max_city = city  # 최대 인구를 가진 도시 갱신
    if city[1] < min_pop:
        min_pop = city[1]  # 최소 인구 갱신
        min_city = city  # 최소 인구를 가진 도시 갱신

# 결과 출력
print('최대인구: {0}, 인구: {1} 천명'.format(max_city[0], max_pop[1]))
print('최소인구: {0}, 인구: {1} 천명'.format(min_city[0], min_pop[1]))
print('리스트 도시 평균 인구: {0} 천명'.format(total_pop / len(city_info)))
