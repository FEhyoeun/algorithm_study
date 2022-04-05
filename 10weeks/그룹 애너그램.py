class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {} # 빈 딕셔너리 생성

        for str in strs: # strs를 순회하면서
            key = ''.join(sorted(str)) # 알파벳 순으로 정렬한 값을 key 변수에 넣는다.
            print(key, str)
            if key not in dict: dict[key] = [str] # 그리고 그 값이 dict에 포함되지 않았다면 -> 그 값을 key로 하고, 원본 str를 value로 하는 dict 만듦.
            else: dict[key].append(str) # 포함되었다면 -> 그 값을 key로 하는 value에 str를 추가.

        return dict.values() # dict의 value만 return.