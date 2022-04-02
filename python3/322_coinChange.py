class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def helper(remain):
            if remain == 0:
                return 0
            if remain < 0:
                return float('inf')
            Min = float('inf')
            for c in coins:
                Min = min(1+helper(remain-c), Min)
            return Min
        res = helper(amount)
        return res if res != float('inf') else -1