class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def feasible(cap):
            day = 1
            cur = 0
            for w in weights:
                cur += w
                if cur > cap:
                    cur = w
                    day += 1
                if day > days:
                    return False
            
            return True
        
        l, r = max(weights), sum(weights)
        while l < r:
            mid = l + (r-l)//2
            if feasible(mid):
                r = mid
            else:
                l = mid + 1
        return l