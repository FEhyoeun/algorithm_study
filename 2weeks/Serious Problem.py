n = int(input())
s = input()
print(2 if s.count('2') > s.count('e') else 'e' if s.count('2') < s.count('e') else 'yee')