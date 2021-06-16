class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        result: accepted
        naive solution: check the board based on the rules
        runtime: O(1), space: O(1)
        """
        #check horizontal
        for r in range(9):
            s = set()
            for c in range(9):
                if board[r][c] != ".":
                    if board[r][c] in s:
                        return False
                    else: 
                        s.add(board[r][c])
        #check vertical
        for r in range(9):
            s = set()
            for c in range(9):
                if board[c][r] != ".":
                    if board[c][r] in s:
                        return False
                    else: 
                        s.add(board[c][r])
        #checkc box
        start = [(0,0), (3,0), (6,0), (0,3), (0,6), (3,3), (3,6), (6,0), (6,3), (6,6)]
        for x,y in start:
            s = set()
            for i in range(3):
                for j in range(3):
                    r, c = i+x, j+y
                    if board[r][c] != ".":
                        if board[r][c] in s:
                            return False
                        else: 
                            s.add(board[r][c])
        return True