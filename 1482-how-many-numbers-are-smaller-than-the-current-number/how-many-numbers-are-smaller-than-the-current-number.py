class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = {}
        sorted_num = sorted(nums)
        for i, num in enumerate(sorted_num):
            if num not in res:
                res[num] = i
        return [res[num] for num in nums]

      
    