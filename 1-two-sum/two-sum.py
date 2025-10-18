class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            sec = target - nums[i]
            if sec in dict:
                return dict[sec], i
            else:
                dict[nums[i]] = i
            

            
        