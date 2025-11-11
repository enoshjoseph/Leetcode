class Solution:
    def lengthOfLastWord(self, s: str) -> int:
       count = 0
       s = s.strip()
       for i in range(len(s)):
        if s[i] == " ":
            count = 0
        else:
            count += 1
       return count