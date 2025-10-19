class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        lpow = 3 ** 19
        return n >0 and lpow % n == 0