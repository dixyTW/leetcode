class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        result: accepted
        straight forward solution: swap 4 numbers based on the pattern
        visual representation
        1   2   3
        
        4   5   6
        
        7   8   9
        we want to swap 1 -> 3, 3 -> 9, 9 -> 7, 7 -> 1
        the four locations can always be represented with one, two, three, four below 
        runtime: O(n^2)
        """
        # col = len(matrix)//2+1 if len(matrix)%2 else len(matrix)//2
        # for i in range(col):
        #     for j in range(i, len(matrix)-i-1):
        #         one = matrix[i][j]
        #         two = matrix[j][len(matrix)-i-1]
        #         three = matrix[len(matrix)-i-1][len(matrix)-j-1]
        #         four = matrix[len(matrix)-j-1][i]
        #         matrix[i][j], matrix[j][len(matrix)-i-1], matrix[len(matrix)-i-1][len(matrix)-j-1], matrix[len(matrix)-j-1][i] = four, one, two, three
                
        """
        result: accepted
        cheat solution
        runtime: O(n^2)
        """
        matrix.reverse()
        for r in range(len(matrix)):
            for c in range(r):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]