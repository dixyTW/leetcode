class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        """
        bottom-up dp
        """
        N = len(arr)
        dp = [[float('inf') for _ in range(N)] for _ in range(N)]
        for i in range(N):
            dp[i][i] = 0
        for i in range(N-1, -1, -1):
            for j in range(i, N):  
                if j-i >= 1:  
                    for k in range(i, j):
                        rootVal = max(arr[i:k+1]) * max(arr[k+1:j+1])
                        dp[i][j] = min(dp[i][j], rootVal + dp[i][k] + dp[k+1][j])
        return dp[0][N-1]
        
        """
        top bottom dp
        """
#         @lru_cache(None)
#         def helper(l, r):
#             if l+1 >= r:
#                 return 0
#             ans = float('inf')
#             for i in range(l+1, r):
#                 rootVal = max(arr[l:i]) * max(arr[i:r])
#                 ans = min(ans, rootVal + helper(l,i) + helper(i,r))
#             return ans
#         return helper(0, len(arr))
    