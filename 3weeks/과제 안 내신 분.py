arr = list(range(1, 31))

while True:
  n = int(input())
  arr.remove(n)
  if len(arr) < 3: break

print(arr[0])
print(arr[1])