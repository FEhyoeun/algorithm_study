a, b, c, d = list(map(int, input().split()))
while True:
  if a == 0 and b == 0 and c == 0 and d == 0:
    break
  else:
    print(c-b,d-a)
    a, b, c, d = list(map(int, input().split()))