S = 'bacaAacba'
T = 'abc'

from collections import Counter

def isAnagram(first, second):
  if first == second: return True

def solution():
  counter = sorted(Counter(T).items())
  length = len(T)
  t = sum = 0

  while length+t <= len(S):
    temp = sorted(Counter(S[t:length+t]).items())
    t += 1
    if isAnagram(temp, counter): sum += 1
    temp = 0

  return sum

solution()