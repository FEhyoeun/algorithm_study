T = int(input()) # 테이스 케이스의 개수

for _ in list(range(T)):
  N = int(input()) # 자연수 개수
  N_list = list(map(int, input().split())) # N개의 자연수
  print(sum(N_list))
