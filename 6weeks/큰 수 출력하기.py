N = int(input())
number_list = list(map(int, input().split()))
answer_list = []

def isBigger(first_number, second_number):
  if first_number < second_number: return True

for i in range(N-1):
  if i == 0: answer_list.append(number_list[i])
  elif isBigger(number_list[i],number_list[i+1]):
    answer_list.append(number_list[i+1])

print(' '.join(str(_) for _ in answer_list))
