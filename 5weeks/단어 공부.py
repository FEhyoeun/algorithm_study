# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

from string import ascii_uppercase

word = input()
word = word.upper() # 대문자로 바꿔줌
alpabet_list = list(ascii_uppercase)
count_list = []

for i in alpabet_list:
  count_list.append(word.count(i)) # 주어진 word를 알파벳 리스트의 알파벳과 비교해서 카운트를 함


if count_list.count(max(count_list)) >= 2: # count_list에서 최대값을 구해서 그게 2 이상인 경우(가장 많이 사용된 알파벳이 여러 개인 경우) '?'' 출력
  print('?')
else: # 그게 아니면 최대값의 index를 구함. 그리고 그 index의 값의 위치에 있는 alpabet_list의 값을 출력함(왜냐하면 alpabet_list랑 count_list의 index 위치가 똑같으니까.)
  print(alpabet_list[count_list.index(max(count_list))])
