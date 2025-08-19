class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxLen=left=right = 0
        for i in s:
            if i == "(":
                left += 1
            else:
                right += 1
            
            if left == right:
                
                maxLen = max(maxLen, left * 2)
            elif right > left:
                left = 0
                right = 0
        
        left = right = 0
        for i in range(len(s) - 1, -1, -1):
            if  s[i] == "(":
                left += 1
            
            else:
                right += 1
            
            if left == right:
                maxLen = max(maxLen, left * 2)
            elif left > right:
                left = 0
                right = 0
        return maxLen