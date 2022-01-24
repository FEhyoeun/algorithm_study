arr = []
for i in list(range(8)):
  if i % 2 == 0: arr.append(input()[::2]) # 그냥 2칸 간격으로(흰색이 첫 칸일 때)
  else: arr.append(input()[1::2]) # 인덱스 1부터 2칸 간격으로(흰색이 두 번째 칸일 때)

print(''.join(arr).count('F'))