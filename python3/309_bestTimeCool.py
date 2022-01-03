class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        dif = [0] + [prices[i] - prices[i-1] for i in range(1, N)]
        dp, dp_max = [0 for _ in range(N+2)], [0 for _ in range(N+2)]
        for i in range(N):
            dp[i] = dif[i] + max(dp[i-1], dp_max[i-3])
            dp_max[i] = max(dp_max[i-1], dp[i])
        return dp_max[-3]