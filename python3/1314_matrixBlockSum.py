class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        def helper(m,r,c):
            # calculates the sum given the cordinates
            
            #r2,c2 bottom right corner, r1,c1 upper left corner
            r2,c2,r1,c1 = min(M, r+k), min(N, c+k), max(r-k-1, 0), max(c-k-1, 0)
            return preSum[r2][c2] - preSum[r2][c1] - preSum[r1][c2] + preSum[r1][c1]
            
        M, N = len(mat), len(mat[0])
        preSum = [[0 for _ in range(N+1)] for _ in range(M+1)]
        for r in range(1,M+1):
            for c in range(1,N+1):
                preSum[r][c] = mat[r-1][c-1] + preSum[r][c-1] + preSum[r-1][c] - preSum[r-1][c-1]
                
        ans = [[0 for _ in range(N)] for _ in range(M)]
        for r in range(M):
            for c in range(N):
                ans[r][c] = helper(preSum,r+1,c+1)
        return ans
        
