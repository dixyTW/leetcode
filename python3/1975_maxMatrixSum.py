class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        M, N = len(matrix), len(matrix[0])
        neg = 0
        Sum = 0
        zeroes = 0
        Min = float('inf')
        for r in range(M):
            for c in range(N):
                if matrix[r][c] != 0:
                    if matrix[r][c] < 0:
                        neg += 1
                    num = abs(matrix[r][c])
                    Sum += num
                    Min = min(num, Min)
                else:
                    zeroes += 1
        
        if zeroes > 0 or not neg%2:
            return Sum
        else:
            return Sum - Min*2