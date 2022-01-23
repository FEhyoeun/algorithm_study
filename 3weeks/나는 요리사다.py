participant_list = []

for _ in list(range(1, 6)):
  participant_list.append(sum(list(map(int, input().split()))))

max_value = max(participant_list)
print(participant_list.index(max_value)+1, max_value)