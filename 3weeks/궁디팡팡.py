N = int(input())
arr = list(map(int, input().split()))
bbadda_len = 0
for i in list(range(1, N+1)):
  if i != arr[i-1]:
    bbadda_len += 1

print(bbadda_len)