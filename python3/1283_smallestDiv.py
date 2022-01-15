class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def feasible(div):
            return sum([math.ceil(n/div) for n in nums]) <= threshold
        l, r = 1, sum(nums)
        while l < r:
            mid = l + (r-l)//2
            if feasible(mid):
                r = mid
            else:
                l = mid + 1
        return l