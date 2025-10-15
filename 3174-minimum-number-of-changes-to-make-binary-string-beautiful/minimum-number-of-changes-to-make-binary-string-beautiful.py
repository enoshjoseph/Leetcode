class Solution:
    def minChanges(self, s: str) -> int:
        flip = 0
        for i in range(0,len(s), 2):
            if i + 1 < len(s) and s[i] != s[i+1]:
                flip += 1
        return flip
        