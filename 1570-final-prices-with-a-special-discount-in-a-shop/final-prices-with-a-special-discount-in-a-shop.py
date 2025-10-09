class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        
        n = len(prices)
        res = [0] * n
        for i in range(n-1,-1,-1):
            while len(stack) != 0 and stack[-1] > prices[i]: 
                stack.pop()
            if len(stack) != 0:
                res[i] =  prices[i] - stack[-1]
            else:
                res[i] = prices[i]
            
            stack.append(prices[i])
        return res