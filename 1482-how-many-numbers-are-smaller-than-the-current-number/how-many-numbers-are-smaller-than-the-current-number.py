class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        N  = len(nums)
        ans = [0] * N
        for i in range(N):
            for j in range(N):
                if i != j and  nums[j] < nums[i]:
                    ans[i] += 1
        return ans
                    
                   