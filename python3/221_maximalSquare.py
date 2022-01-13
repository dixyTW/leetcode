class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        M, N = len(matrix), len(matrix[0])
        ans = 0
        for r in range(M):
            for c in range(N):
                matrix[r][c] = int(matrix[r][c])
                if matrix[r][c]:
                    ans = 1 

        for r in range(1,M):
            for c in range(1,N):
                matrix[r][c] = min(matrix[r-1][c], matrix[r][c-1], matrix[r-1][c-1])+matrix[r][c] if matrix[r][c] else 0
                ans = max(matrix[r][c],ans)
        return ans**2
        