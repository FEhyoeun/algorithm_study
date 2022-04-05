class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 팰린드롬 판별 및 투 포인터 확장. 가운데부터 시작해서 left는 점점 왼쪽으로, right는 점점 오른쪽으로
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        # 한글자이거나 토마토(ㅋㅋ)처럼 단어 자체가 회문일 때
        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''

        # 슬라이딩 윈도우 우측으로 이동
        for i in range(len(s)):
            # max(기존 result, 짝수일 때, 홀수일 때)
            result = max(result, expand(i, i + 1), expand(i, i + 2), key = len) # key = len이면 문자열 길이가 가장 큰 것을 반환하고, 그런 게 여러 개 있을 경우 index가 작은 것을 반환함
        return result