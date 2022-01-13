class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        M, N = len(matrix), len(matrix[0])
        self.m = [[0 for _ in range(N+1)] for _ in range(M+1)]
        for r in range(1,M+1):
            for c in range(1,N+1):
                self.m[r][c] = self.m[r][c-1] + matrix[r-1][c-1]
        
        for r in range(1,M+1):
            for c in range(1,N+1):
                self.m[r][c] += self.m[r-1][c]
                

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.m[row2+1][col2+1] - self.m[row2+1][col1] - self.m[row1][col2+1] + self.m[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)