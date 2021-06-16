class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        result: accepted
        backtracking: when we encounter a empty slot, try every number and check if the number will
        be valid or not, if a number is not valid, we backtrack and try another number
        """
        self.solve(board)
        
    def nextPos(self,board):
        """
        helper function that finds the next empty slot, if all slot are filled, return -1,-1
        """
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    return r, c
        return -1, -1
    
    
        
    def solve(self, board) -> bool:
        nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        r, c = self.nextPos(board)
        if r == -1 and c == -1: 
            return True
        for num in nums:
            #tricky part
            if self.isValid(board, r, c, num):
                board[r][c] = num
                if self.solve(board):
                    return True
                board[r][c] = "."
        
    
 
    def isValid(self, board, r, c, num) -> bool:
        """
        check if the inserted number is valid
        """
        row_s = {num}
        for i in range(9):
            #check row
            if board[i][c] != ".":
                if board[i][c] in row_s:
                    return False
                else:
                    row_s.add(board[i][c])
                    
        col_s = {num}
        for i in range(9):
            #check col
            if board[r][i] != ".":
                if board[r][i] in col_s:
                    return False 
                else:
                    col_s.add(board[r][i])
        
        box_s = {num}
        box_r, box_c = (r//3)*3, (c//3)*3
        for x in range(3):
            for y in range(3):
                row, col = box_r + x, box_c + y
                if board[row][col] != ".":
                    if board[row][col] in box_s:
                        return False
                    else:
                        box_s.add(board[row][col])

        return True