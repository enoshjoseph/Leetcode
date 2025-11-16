class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        N = len(nums)
        nums = set(nums)
        ans = []
        for i in range(1, N+1):
            if i not in nums:
                ans.append(i)
                
        return ans
                
        