class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def feasible(n): 
            count = 1 # number of partitions
            cur = 0 # current sum of the partition
            for num in nums:
                cur += num
                if cur > n:
                    count += 1
                    cur = num
                if count > m:
                    return False
            return True 
            # we don't care if number of partition is exactly count == m because
            # if count < m, we can guarantee that size n of partition can split the array 
            # into m partitions, think of the extreme case n = sum(nums)
        
        l, r = max(nums), sum(nums)
        while l < r:
            mid = l + (r-l)//2
            if feasible(mid):
                r = mid
            else:
                l = mid + 1
        return l 
        
#         N = len(nums)
#         @lru_cache(None)
#         def helper(i, n):
#             if i == N:
#                 return 0
#             if n == 0:
#                 return float('inf')

#             ans = float('inf')
#             Sum = 0
#             for j in range(i, N-n+1):
#                 Sum += nums[j]
#                 ans = min(ans, max(Sum, helper(j+1, n-1)))
#             return ans
        
#         return helper(0, m)
    
       