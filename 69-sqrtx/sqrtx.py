class Solution:
    def mySqrt(self, x: int) -> int:
        res = 0
        hi = x
        lo = 1
        while lo <= hi:
            mid = lo + (hi - lo)//2

            if mid * mid <= x:
                res = mid
                lo = mid + 1
        
            else:
                hi = mid - 1
        return res
