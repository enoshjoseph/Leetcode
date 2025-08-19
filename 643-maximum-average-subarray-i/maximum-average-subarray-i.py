class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currentSum = 0
        maxavg = float("-inf")
        for i in range(k):
            currentSum += nums[i]

        maxavg = currentSum/k

        for i in range(k, len(nums)):
            currentSum += nums[i]
            currentSum -= nums[i - k]
            maxavg = max(maxavg, currentSum / k)
        return maxavg