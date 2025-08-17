class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_water = 0
        left, right = 0, len(height) - 1
        while left < right:
            h = min(height[left], height[right])
            width = right - left
            current_water = h * width
            max_water = max(max_water, current_water)

            if height[left] < height[right]: left += 1
            else: right -= 1
        return max_water