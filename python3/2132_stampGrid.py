class Solution:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        def sum_2d(m,r1,c1,r2,c2):
            return m[r2][c2] - m[r2][c1-1] - m[r1-1][c2] + m[r1-1][c1-1]
        
        def make_pre(m, row, col):
            new_m = [[0 for _ in range(col)] for _ in range(row)]
            for r in range(1,row):
                for c in range(1,col):
                    new_m[r][c] = m[r-1][c-1] + new_m[r][c-1] + new_m[r-1][c] - new_m[r-1][c-1]
            return new_m

        M, N = len(grid), len(grid[0])
        H, W = stampHeight, stampWidth
        
        preSum = make_pre(grid, M+1, N+1)        
        canStamp = [[0 for _ in range(N)] for _ in range(M)]
        for r in range(H-1, M):
            for c in range(W-1, N):
                canStamp[r][c] = int(sum_2d(preSum, r-H+2, c-W+2, r+1, c+1) == 0)
        preSum2 = make_pre(canStamp, M+1, N+1)
        for r in range(M):
            for c in range(N):
                if grid[r][c] == 0 and sum_2d(preSum2, r+1, c+1, min(M, r+H), min(N, c+W)) == 0:
                    return False
        return True
        
        