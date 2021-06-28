class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        result: accepted
        backtrack solution: simulate each queen placed on the board, and backtrack if the placed queen doesn't work out
        runtime: O(n^n), space: O(n^2)
        """
        self.ans = []
        board = ["."*n for _ in range(n)]
        def helper(queens, board, r):
            if not queens:
                self.ans.append(copy.deepcopy(board))
                return
            for i in range(n):
                if is_valid(board, r, i):
                    board[r] = board[r][:i] + "Q" + board[r][i+1:] #can improve the slicing part with an actual 2d array, and making the 2d array into a proper solution at the end
                    helper(queens-1, board, r+1)
                    board[r] = board[r][:i] + "." + board[r][i+1:]
            
            
        
        def is_valid(board, r, c):
            #helper function that checks if placing a queen ensures the queen is safe
            res = True
            #check horizontal, extra in this case since we always move onto the next row if a queen is placed
            if "Q" in board[r]:
                res = False
            #check diagonal 4 directions
            for i in range(n):
                if (0 <= r-c+i < n and board[r-c+i][i] == "Q") or (0 <= r+c-i < n and board[r+c-i][i] == "Q"):
                    res = False
            #check vertical
            for s in board:
                if s[c] == "Q":
                    res = False
            return res
        helper(n, board, 0)
        return self.ans
            