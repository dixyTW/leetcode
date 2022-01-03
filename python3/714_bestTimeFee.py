class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        tik0, tikold, tik1, = 0, 0, float('-inf')
        for p in prices:
            tikold = tik0
            tik0 = max(tik0, tik1+p-fee)
            tik1 = max(tik1, tikold-p)
        return tik0
            