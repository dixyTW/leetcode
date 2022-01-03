class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        greedy solution
        """
        buy = float('inf')
        ans = 0
        for p in prices:
            if p > buy:
                ans += p - buy
                buy = float('inf')
            if p < buy:
                buy = p
        return ans 