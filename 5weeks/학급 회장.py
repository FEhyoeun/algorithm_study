candidate_list = ['A', 'B', 'C', 'D', 'E'] # 후보 리스트
votes_number_list = [] # 득표수 리스트

_ = int(input())
vote_list = list(input()) # 투표 리스트

for i in candidate_list:
  votes_number_list.append(vote_list.count(i))

max_value_index = votes_number_list.index(max(votes_number_list))

print(candidate_list[max_value_index])