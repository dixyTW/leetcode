class Solution:
    def countElements(self, nums: List[int]) -> int:
        """
        sort O(nlogn)
        """
#         N = len(nums)
#         nums.sort()
#         l, r = 1, N-2
#         while l < N and nums[l] == nums[l-1]:
#             l += 1
        
#         while r > 0 and nums[r] == nums[r+1]:
#             r -= 1
            
#         return r-l+1 if r-l+1 > 0 else 0
        
        """
        min/max O(n)
        """
        Min, Max = min(nums), max(nums)
        cnt = 0
        for num in nums:
            if Min < num < Max:
                cnt += 1
        return cnt