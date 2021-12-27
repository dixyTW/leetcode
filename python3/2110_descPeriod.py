class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:           
        lst = []
        ans = 0
        i = 1
        og = 0
        while i < len(prices):
            og = i-1
            while i < len(prices) and prices[i] - prices[i-1] == -1:
                i += 1
            lst.append(i-og)
            i += 1
        if sum(lst) != len(prices):
            lst.append(len(prices) - sum(lst))
        for num in lst:
            ans += sum(range(1,num+1))
        return ans
