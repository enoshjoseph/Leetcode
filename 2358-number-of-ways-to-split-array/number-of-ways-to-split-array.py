class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        leftSum = 0
        totalSum = sum(nums)
        count = 0
        for i in range(len(nums)-1):
            leftSum +=  nums[i]
            
            if leftSum >= totalSum-leftSum:
                count += 1
        return count