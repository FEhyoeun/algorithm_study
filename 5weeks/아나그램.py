first_word = input() # 첫 번째 단어 받기
second_word = input() # 두 번째 단어 받기

# 각 단어에서 알파벳만 뽑아내기
def getAlphabetFromWords(first_word, second_word):
  return [set(list(first_word)), set(list(second_word))]

# 뽑아낸 알파벳을 key, 그 key의 count를 value 값으로 하는 딕셔너리로 만들기
def setHashFromWords(first, second):
  first_hash = {}
  second_hash = {}
  for i in first:
    first_hash[i] = first_word.count(i)

  for i in second:
    second_hash[i] = second_word.count(i)

  return [first_hash, second_hash]

# 아나그램인지 판별
def isAnagram(first_hash, second_hash):
  print('YES' if first_hash == second_hash else 'NO')

first, second = getAlphabetFromWords(first_word, second_word)
first_hash, second_hash = setHashFromWords(first, second)

isAnagram(first_hash, second_hash)