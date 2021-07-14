class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        result: AC
        constant space: use first row and first col to store information about other columns
        runtime: O(mn), space: O(1)
        """
        first_row, first_col = False, False
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                first_col = True
                break
        
        for i in range(len(matrix[0])):
            if matrix[0][i] == 0:
                first_row = True
                break
                
        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                if matrix[r][c] == 0:
                    matrix[r][0], matrix[0][c] = 0, 0

        
        for i in range(1,len(matrix)):
            if matrix[i][0] == 0:
                for c in range(len(matrix[0])):
                    matrix[i][c] = 0
        
        for i in range(1,len(matrix[0])):
            if matrix[0][i] == 0:
                for r in range(len(matrix)):
                    matrix[r][i] = 0
        
        if first_col:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        if first_row:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
        