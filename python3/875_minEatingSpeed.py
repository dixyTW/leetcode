class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def greedy(k):
            hour = 0
            for p in piles:
                hour += math.ceil(p/k)
                
            if hour > h:
                return False
            return True

     
        l, r = 1, max(piles)
        while l < r:
            mid = l + (r-l)//2
            if greedy(mid):
                r = mid
            else:
                l = mid + 1
        return l