class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = csum = 0
        size = len(nums) + 1

        for r in range(len(nums)):

            csum += nums[r]

            while csum >= target:
                size = min(size, (r - left + 1))
                csum -= nums[left]
                left += 1

        return size if size != len(nums) + 1 else 0
        