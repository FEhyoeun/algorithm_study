A, B, C = list(map(int, input().split())) # 한손, 노룩, 폰
N = int(input()) # 참가한 동아리 수
competition_sum_list = [] # 동아리별 점수 합산 리스트
temp_list = []

for _ in list(range(3*N)):
  a, b, c = list(map(int, input().split())) # 참가자 한 명의 기술 횟수
  temp_list.append(A*a + B*b + C*c)

for i in list(range(N)):
  competition_sum_list.append(sum(temp_list[3*i:3*(i+1)]))

print(max(competition_sum_list))
