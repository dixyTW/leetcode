class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def enough(x):
            cnt = 0 #number of nums that's less than x
            for r in range(1,m+1):
                cnt += min(x//r, n)
                if cnt >= k:
                    return True
            return False
        
        l, r = 1, m*n
        while l < r:
            mid = l + (r-l)//2

            if enough(mid):
                r = mid
            else:
                l = mid + 1
        return l