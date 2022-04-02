class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        N = len(piles)
        @lru_cache(None)
        def helper(index, cnt):
            if index == N:
                if cnt == 0:
                    return 0
                if cnt > 0:
                    return float('-inf')
            ans = helper(index+1, cnt)
            sm = 0
            for i in range(min(len(piles[index]), cnt)):
                sm += piles[index][i]
                ans = max(ans, sm + helper(index+1, cnt-(i+1)))
            return ans
        return helper(0, k)