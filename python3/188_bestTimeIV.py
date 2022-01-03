class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) <= 1 or k == 0:
            return 0
        k = min(k, math.ceil(len(prices)/2))
        tik0 = [0 for _ in range(k+1)]
        tik1 = [float('-inf') for _ in range(k+1)]
        for p in prices:
            for i in range(k):
                tik0[i] = max(tik0[i], tik1[i]+p)
                tik1[i] = max(tik1[i], tik0[i-1]-p)
        return tik0[-2]