class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        totalsum = sum(nums)
        left_sum = 0
        ans = 0

        for x in nums:
            if x==0:
                right = totalsum - left_sum

                if left_sum == right:
                    ans+= 2
                elif abs(left_sum - right) == 1:
                    ans += 1
            else:
                left_sum += x
        return ans

        