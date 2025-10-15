class Solution:
    def minChanges(self, s: str) -> int:
        flip = 0
        for i in range(0,len(s), 2):
            window = s[i:i+2]
            flip += min(window.count("0"), window.count("1"))
        return flip
        