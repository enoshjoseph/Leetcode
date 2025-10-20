class Solution:
    def canCross(self, stones: List[int]) -> bool:
       dp = {stone : set() for stone in stones}
       stones_set = set(stones)
       dp[0].add(0)
       for stone in stones:
        for j in dp[stone]:
            for step in [j-1, j, j+1]:
                if step > 0 and (step + stone) in stones_set:
                    dp[step +stone].add(step)
       return len(dp[stones[-1]]) > 0