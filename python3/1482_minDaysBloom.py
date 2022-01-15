class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def feasible(d):
            days, f, b = 0, 0, 0
            
            for day in bloomDay:
                if day <= d:
                    f += 1
                else:
                    f = 0
                if f == k:
                    b += 1
                    f = 0
            return b >= m
                
        if len(bloomDay) < m*k:
            return -1
        l, r = 1, max(bloomDay)
        while l < r:
            mid = l + (r-l)//2
            if feasible(mid):
                r = mid
            else:
                l = mid + 1
        return l