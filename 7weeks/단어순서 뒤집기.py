N = int(input()) # 전체 케이스 개수
word_dict = {} # 입력 받은 단어를 넣을 딕셔너리. key는 케이스, value는 입력 받은 단어.

for i in range(N):
  word_dict[i+1] = input()

for key, value in word_dict.items(): # 위의 word_dict를 반복하면서 key와 value를 모두 활용
  split_word_list = value.split( ) # 단어를 띄어쓰기 단위로 쪼개서 배열에 넣어줌
  temp_list = []
  for index in reversed(range(len(split_word_list))): # 띄어쓰기 단위로 단어를 쪼갠 리스트의 index를 활용. 역순으로.
    temp_list.append(split_word_list[index]) # 그걸 임시 배열에 담기.
  print('Case #%d:' % key, ' '.join(temp_list)) # 문제 형식에서 원하는대로 출력