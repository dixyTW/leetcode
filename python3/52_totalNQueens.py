class Solution:
    def totalNQueens(self, n: int) -> int:
        """
        result: accepted
        dfs backtracking
        runtime: O(n^n), space: O(n)
        """
        board = [-1 for _ in range(n)]
        self.ans = 0
        def helper(board, index):
            if index == len(board):
                #finished traversing the board, the board is valid
                self.ans += 1
                return
            for i in range(n):
                if is_valid(board, index, i):
                    #if the queen is valid at position (index, i) place the queen and move on to the next row, backtrack after function returns
                    board[index] = i 
                    helper(board, index+1)
                    board[index] = -1
            
        def is_valid(board, r, c):
            #check if queen placed at board[r][c] is safe
            
            #check vertical and diagnal (check diagnal by checking the slope of two points)
            for i, num in enumerate(board):
                if num == c or (board[i] != -1 and abs((c-num)/(r-i)) == 1) :
                    return False
            
            return True
            
        
        helper(board, 0)
        return self.ans