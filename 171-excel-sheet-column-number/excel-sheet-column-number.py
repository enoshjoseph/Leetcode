class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        offset = 0
        N = len(columnTitle)
        for i in range(N):
            offset += 26 ** i
        
        ans = 0
        for c in columnTitle:
            ans  *= 26
            ans += ord(c) - ord('A')
        return offset + ans