class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxLen = 0
        stack = []
        stack.append(-1)
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if len(stack) != 0:
                    maxLen = max(maxLen, i - stack[-1])
                
                else:
                    stack.append(i)
        return maxLen
                    
                
