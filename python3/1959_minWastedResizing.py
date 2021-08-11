class Solution:
    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
        """
        source: https://leetcode.com/problems/minimum-total-space-wasted-with-k-resizing-operations/discuss/1389247/C%2B%2BJavaPython-Simple-Top-down-DP-Clean-and-Concise
        runtime: O(n^2*k)
        """
        @lru_cache(None)
        def dp(i, k):
            if i == len(nums):
                return 0
            if k == -1:
                return float("inf")
            ans = float('inf')
            Sum, Max = 0, float("-inf")
            for j in range(i, len(nums)):
                Max = max(Max, nums[j])
                Sum += nums[j]
                wasted = Max*(j-i+1) - Sum
                ans = min(ans, wasted + dp(j+1, k-1))
            return ans
                
        return dp(0, k)
        