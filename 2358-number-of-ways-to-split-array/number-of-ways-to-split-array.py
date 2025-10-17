class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        leftSum = 0
        totalSum = sum(nums)
        count = 0
        for i in range(len(nums)-1):
            leftSum +=  nums[i]
            rightSum =  totalSum - leftSum
            if leftSum >= rightSum:
                count += 1
        return count