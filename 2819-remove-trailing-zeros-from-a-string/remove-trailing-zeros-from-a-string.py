class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        i = len(num) - 1
        while num[i] == "0" and (0 <= i - 1):
            i -= 1
        return num[:i+1]


        