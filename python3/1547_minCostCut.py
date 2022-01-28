class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        cuts = [0] + cuts + [n]
        N = len(cuts)
        dp = [[0 for _ in range(N)] for _ in range(N)]
        
        for i in range(N-1, -1, -1):
            for j in range(i+1, N):
                for k in range(i+1, j):
                    dp[i][j] = min(float('inf') if dp[i][j] == 0 else dp[i][j], cuts[j] - cuts[i] + dp[i][k] + dp[k][j])
                    
        
        return dp[0][N-1]
        
        
#         cuts.sort()
#         cuts = [0] + cuts + [n]
#         N = len(cuts)
#         @lru_cache(None)
#         def helper(i,j):
#             if i+1 >= j:
#                 return 0
#             ans = float('inf')
#             for k in range(i+1, j):
#                 res = (cuts[j] - cuts[i]) + helper(i, k) + helper(k, j) 
#                 ans = min(res, ans)
#             return ans
#         return helper(0, N-1)

#         cuts.sort()
#         N = len(cuts)
#         @lru_cache(None)
#         def helper(l,r,cuts_l,cuts_r):
#             if r <= l+1 or cuts_r < cuts_l:
#                 return 0
#             ans = float('inf')
#             for k in range(cuts_l, cuts_r+1):
#                 loc = cuts[k]
#                 res = helper(l, loc, cuts_l, k-1) + helper(loc, r, k+1, cuts_r) + r-l
#                 ans = min(res, ans)
#             return ans
#         return helper(0, n, 0, N-1)
    
        
            