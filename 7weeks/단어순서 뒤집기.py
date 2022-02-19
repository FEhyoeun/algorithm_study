# 스페이스로 띄어쓰기 된 단어들의 리스트가 주어질때, 단어들을 반대 순서로 뒤집어라. 각 라인은 w개의 영단어로 이루어져 있으며, 총 L개의 알파벳을 가진다. 각 행은 알파벳과 스페이스로만 이루어져 있다. 단어 사이에는 하나의 스페이스만 들어간다.

# 입력
# 첫 행은 N이며, 전체 케이스의 개수이다.

# N개의 케이스들이 이어지는데, 각 케이스는 스페이스로 띄어진 단어들이다. 스페이스는 라인의 처음과 끝에는 나타나지 않는다. N과 L은 다음 범위를 가진다.

# N = 5
# 1 ≤ L ≤ 25
# 출력
# 각 케이스에 대해서, 케이스 번호가 x일때  "Case #x: " 를 출력한 후 그 후에 이어서 단어들을 반대 순서로 출력한다.


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