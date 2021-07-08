class Solution:
    def mySqrt(self, x: int) -> int:
        """
        result: accepted
        binary search
        runtime: (O(logx)), space: O(1)
        """
        l, r = 1, x
        if x == 0 or x == 1:
            return x
        while l < r:
            mid = (l+r)//2
            if mid**2 <= x:
                l = mid + 1
            else:
                r = mid -1
        if l**2 > x:
            return l -1
        else:
            return l