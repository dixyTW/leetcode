class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        N = len(nums)
        def feasible(dif):
            l, r = 0, 0
            cnt = 0
            while r < N or l < N:
                while r < N and nums[r] - nums[l] <= dif:
                    r += 1
                cnt += r-l-1 #account for r+1
                l += 1
            return cnt >= k
        nums.sort()
        l, r = 0, max(nums)-min(nums)
        while l < r:
            
            mid = l + (r-l)//2

            if feasible(mid):
                r = mid
            else:
                l = mid + 1
        return l
        